# flashing_effect.py

import time


def get_flash_color(
    is_flashing, flash_start_time, original_color, flash_color, flash_duration=2
):
    if is_flashing:
        # Calculate elapsed time since flash started
        elapsed_time = time.time() - flash_start_time
        # Determine if we should be showing the original color or white
        if int(elapsed_time * 10) % 2 == 0:
            color = original_color
        else:
            color = flash_color
        # End flashing after the flash duration
        if elapsed_time > flash_duration:
            is_flashing = False
    else:
        color = original_color

    return color, is_flashing
