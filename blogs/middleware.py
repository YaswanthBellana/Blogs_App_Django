"""
Custom middleware for error handling using custom exceptions.
"""
from django.shortcuts import render
from django.http import HttpResponse, Http404
from blogs.exceptions import CustomError, PageNotFoundError, ServerError
import logging

logger = logging.getLogger(__name__)


class ExceptionMiddleware:
    """
    Middleware to handle custom exceptions and display custom error pages.
    Supports both custom exceptions and standard HTTP errors.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return self._handle_response(request, response)
        except CustomError as e:
            logger.error(f"CustomError: {e.message}", exc_info=True)
            return render(
                request,
                self._get_error_template(e.status_code),
                {'error': e.message},
                status=e.status_code
            )
        except Http404:
            logger.warning(f"Page not found: {request.path}")
            return render(request, '404.html', status=404)
        except Exception as e:
            logger.error(f"Unhandled exception: {str(e)}", exc_info=True)
            return render(request, '500.html', {'error': str(e)}, status=500)

    def _handle_response(self, request, response):
        """Handle response status codes."""
        if response.status_code == 404:
            logger.warning(f"404 Page not found: {request.path}")
            return render(request, '404.html', status=404)
        elif response.status_code == 500:
            logger.error(f"500 Server error: {request.path}")
            return render(request, '500.html', status=500)
        return response

    def _get_error_template(self, status_code):
        """Get the appropriate error template based on status code."""
        if status_code == 404:
            return '404.html'
        elif status_code == 500:
            return '500.html'
        else:
            return '500.html'

    def process_exception(self, request, exception):
        """
        Handle exceptions raised during view processing.
        """
        if isinstance(exception, CustomError):
            logger.error(f"CustomError caught: {exception.message}", exc_info=True)
            return render(
                request,
                self._get_error_template(exception.status_code),
                {'error': exception.message},
                status=exception.status_code
            )
        elif isinstance(exception, PageNotFoundError):
            logger.warning(f"PageNotFoundError: {exception.message}")
            return render(request, '404.html', {'error': exception.message}, status=404)
        elif isinstance(exception, ServerError):
            logger.error(f"ServerError: {exception.message}", exc_info=True)
            return render(request, '500.html', {'error': exception.message}, status=500)
        else:
            logger.error(f"Unhandled exception: {type(exception).__name__}: {str(exception)}", exc_info=True)
            return render(request, '500.html', {'error': str(exception)}, status=500)


# Keep backward compatibility with old class name
class CustomErrorMiddleware(ExceptionMiddleware):
    """Backward compatibility wrapper."""
    pass