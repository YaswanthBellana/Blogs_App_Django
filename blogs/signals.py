"""
Signal handlers for the blogs application.
Handles request lifecycle monitoring and error tracking.
"""
from django.core.signals import request_started, request_finished
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)


@receiver(request_started)
def log_request_started(sender, **kwargs):
    """
    Signal handler for request_started.
    Logs when a request starts - useful for monitoring and debugging request flow.
    
    This is part of Option 4: Using Django Signals for error monitoring.
    """
    logger.debug("HTTP Request started")


@receiver(request_finished)
def log_request_finished(sender, **kwargs):
    """
    Signal handler for request_finished.
    Logs when a request completes - useful for performance tracking and monitoring.
    
    This is part of Option 4: Using Django Signals for error monitoring.
    """
    logger.debug("HTTP Request finished successfully")
