"""
Flask config script for error_spike.
"""

class Config(object):
    """
    Production Configuration.
    """
    DEBUG = False

class DevelopmentConfig(Config):
    """
    Development Configuration.
    """
    DEBUG = True
