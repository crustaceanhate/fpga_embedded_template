"""Small fixed-point helpers shared by software and verification code."""


def signed_wrap(value: int, width: int) -> int:
    """Wrap an integer to a two's-complement signed word of *width* bits."""
    if width <= 0:
        raise ValueError("width must be positive")
    mask = (1 << width) - 1
    value &= mask
    sign_bit = 1 << (width - 1)
    return value - (1 << width) if value & sign_bit else value
