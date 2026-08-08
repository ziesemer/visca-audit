# Zowietek ZowieKBD

<https://zowietek.com/product/ptz-camera-keyboard-controller/>

## Observations

1. PTZ Controls:
	1. ⚠️ Pan & Tilt: Limited to 8 levels of speed in any direction of an expected 24.
		1. Range of those speeds are configurable by using the speed dial.
	2. ⚠️ Zoom: Limited to 4 levels of speed in either direction of an expected 8.
		1. Range of those speeds are configurable by using the speed dial.
	3. ⚠️ Overall PTZ coverage score: 40.63%.
2. ⚠️ No "Quick Call" feature for presets - all presets require at least 2 button presses.
3. ⚠️ Startup time is abnormally long.
Unit is unable to send the first packet until 43 seconds after power-on / power supplied.
It takes until almost a full minute has passed for the display to populate and the unit to be fully usable.

There is also a feature when connected to the device through the web UI that should allow for connection of an XBox Controller as a peripheral.
I have not been able to get this working, despite having a game controller connected and recognized by other web pages.

### Support

✅ Support has been very responsive, including an initial firmware revision received within 3 days of first request.

## Related Hardware

The joystick appears to be the same joystick used on the [Tenveo TEVO-KB200MAX](Tenveo-TEVO-KB200MAX.md), including a matching limited resolution of 8 levels on the joystick in any direction.

## Firmware Version Tested

Tested: 2026-08-01

| | Version |
| --- | --: |
| Hardware version | 14.1.3.00 |
| Software version | 2.0.0.42 |
| Serial Number | ***** |
| Model | ZowieKBD |
| Keyboard Panel | 1.1.34 |
| NDI | 5.5.4 |

## Raw Test Results

```text
visca_audit.py 2026-08-01

power on time:
  time: 43.13s

pan left:
       Hit min-max/range: 0x02 - 0x18 (02₁₀ - 24₁₀) / 23₁₀.
  Expected min-max/range: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀.
  [_, _, 2, _, 4, _, _, 7, _, 9, _, _, 12, _, 14, _, 16, _, _, _, _, _, _, _, 24]
       Hit min-max/range/coverage: 0x02 - 0x18 (02₁₀ - 24₁₀) / 23₁₀ / 08₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 33.33%

pan right:
       Hit min-max/range: 0x02 - 0x18 (02₁₀ - 24₁₀) / 23₁₀.
  Expected min-max/range: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀.
  [_, _, 2, _, 4, _, _, 7, _, 9, _, _, 12, _, 14, _, 16, _, _, _, _, _, _, _, 24]
       Hit min-max/range/coverage: 0x02 - 0x18 (02₁₀ - 24₁₀) / 23₁₀ / 08₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 33.33%

tilt up:
       Hit min-max/range: 0x02 - 0x18 (02₁₀ - 24₁₀) / 23₁₀.
  Expected min-max/range: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀.
  [_, _, 2, _, 4, _, _, 7, _, 9, _, _, 12, _, 14, _, 16, _, _, _, _, _, _, _, 24]
       Hit min-max/range/coverage: 0x02 - 0x18 (02₁₀ - 24₁₀) / 23₁₀ / 08₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 33.33%

tilt down:
       Hit min-max/range: 0x02 - 0x18 (02₁₀ - 24₁₀) / 23₁₀.
  Expected min-max/range: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀.
  [_, _, 2, _, 4, _, _, 7, _, 9, _, _, 12, _, 14, _, 16, _, _, _, _, _, _, _, 24]
       Hit min-max/range/coverage: 0x02 - 0x18 (02₁₀ - 24₁₀) / 23₁₀ / 08₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 33.33%

zoom tele seesaw:
       Hit min-max/range: 0x01 - 0x07 (01₁₀ - 07₁₀) / 07₁₀.
  Expected min-max/range: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀.
  [_, 1, _, 3, 4, _, _, 7]
       Hit min-max/range/coverage: 0x01 - 0x07 (01₁₀ - 07₁₀) / 07₁₀ / 04₁₀.
  Expected min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
                    Covered range: 50.00%

zoom wide seesaw:
       Hit min-max/range: 0x01 - 0x07 (01₁₀ - 07₁₀) / 07₁₀.
  Expected min-max/range: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀.
  [_, 1, _, 3, 4, _, _, 7]
       Hit min-max/range/coverage: 0x01 - 0x07 (01₁₀ - 07₁₀) / 07₁₀ / 04₁₀.
  Expected min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
                    Covered range: 50.00%

zoom tele joystick:
       Hit min-max/range: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀.
  Expected min-max/range: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀.
  [0, 1, 2, 3, 4, _, _, 7]
       Hit min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 06₁₀.
  Expected min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
                    Covered range: 75.00%

zoom wide joystick:
       Hit min-max/range: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀.
  Expected min-max/range: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀.
  [0, 1, 2, 3, 4, _, _, 7]
       Hit min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 06₁₀.
  Expected min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
                    Covered range: 75.00%

preset calls:
       Hit min-max/range: 0x00 - 0xfe (00₁₀ - 254₁₀) / 255₁₀.
  Expected min-max/range: 0x00 - 0xfe (00₁₀ - 254₁₀) / 255₁₀.

Total PTZ coverage: 40.63%
```

See also:

* [Testing Approach](../Testing-Approach.md)
