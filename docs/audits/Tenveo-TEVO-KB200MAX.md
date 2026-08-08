# Tenveo TEVO-KB200MAX

<https://www.tenveo.com/product/Controller/462.html>

## Observations

1. PTZ Controls:
	1. ⚠️ Pan & Tilt: Limited to 8 levels of speed in any direction of an expected 24.
		1. Range of those speeds are configurable by using the speed dial.
		2. Tilt is further limited to a maximum speed of only 20 of an expected 24.
	2. ⚠️ Zoom: Limited to 4 levels of speed in either direction of an expected 8.
		1. Range of those speeds are configurable by using the speed dial.
	3. ⚠️ Overall PTZ coverage score: 39.06%.
2. ⚠️ Annoying beep at startup, and does not appear to be configurable.

### Support

Did not attempt any communications with support.

## Related Hardware

The joystick appears to be the same joystick used on the [Zowietek ZowieKBD](Zowietek-ZowieKBD.md), including a matching limited resolution of 8 levels on the joystick in any direction.

## Firmware Version Tested

Tested: 2026-08-03

| | Version |
| --- | --: |
| version | V5.4.8-20251031 |

## Raw Test Results

```text
visca_audit.py 2026-08-01

power on time:
  time: 23.47s

pan left:
       Hit min-max/range: 0x03 - 0x18 (03₁₀ - 24₁₀) / 22₁₀.
  Expected min-max/range: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀.
  [_, _, _, 3, _, _, 6, _, _, 9, _, _, 12, _, _, 15, _, _, 18, _, _, 21, _, _, 24]
       Hit min-max/range/coverage: 0x03 - 0x18 (03₁₀ - 24₁₀) / 22₁₀ / 08₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 33.33%

pan right:
       Hit min-max/range: 0x03 - 0x18 (03₁₀ - 24₁₀) / 22₁₀.
  Expected min-max/range: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀.
  [_, _, _, 3, _, _, 6, _, _, 9, _, _, 12, _, _, 15, _, _, 18, _, _, 21, _, _, 24]
       Hit min-max/range/coverage: 0x03 - 0x18 (03₁₀ - 24₁₀) / 22₁₀ / 08₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 33.33%

tilt up:
       Hit min-max/range: 0x02 - 0x14 (02₁₀ - 20₁₀) / 19₁₀.
  Expected min-max/range: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀.
  [_, _, 2, _, _, 5, _, 7, _, _, 10, _, 12, _, _, 15, _, 17, _, _, 20, _, _, _, _]
       Hit min-max/range/coverage: 0x02 - 0x14 (02₁₀ - 20₁₀) / 19₁₀ / 08₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 33.33%

tilt down:
       Hit min-max/range: 0x02 - 0x14 (02₁₀ - 20₁₀) / 19₁₀.
  Expected min-max/range: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀.
  [_, _, 2, _, _, 5, _, 7, _, _, 10, _, 12, _, _, 15, _, 17, _, _, 20, _, _, _, _]
       Hit min-max/range/coverage: 0x02 - 0x14 (02₁₀ - 20₁₀) / 19₁₀ / 08₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 33.33%

zoom tele seesaw:
       Hit min-max/range: 0x03 - 0x07 (03₁₀ - 07₁₀) / 05₁₀.
  Expected min-max/range: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀.
  [_, _, _, 3, _, 5, _, 7]
       Hit min-max/range/coverage: 0x03 - 0x07 (03₁₀ - 07₁₀) / 05₁₀ / 03₁₀.
  Expected min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
                    Covered range: 37.50%

zoom wide seesaw:
       Hit min-max/range: 0x03 - 0x07 (03₁₀ - 07₁₀) / 05₁₀.
  Expected min-max/range: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀.
  [_, _, _, 3, _, 5, _, 7]
       Hit min-max/range/coverage: 0x03 - 0x07 (03₁₀ - 07₁₀) / 05₁₀ / 03₁₀.
  Expected min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
                    Covered range: 37.50%

zoom tele joystick:
       Hit min-max/range: 0x02 - 0x07 (02₁₀ - 07₁₀) / 06₁₀.
  Expected min-max/range: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀.
  [_, _, 2, 3, 4, 5, 6, 7]
       Hit min-max/range/coverage: 0x02 - 0x07 (02₁₀ - 07₁₀) / 06₁₀ / 06₁₀.
  Expected min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
                    Covered range: 75.00%

zoom wide joystick:
       Hit min-max/range: 0x02 - 0x07 (02₁₀ - 07₁₀) / 06₁₀.
  Expected min-max/range: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀.
  [_, _, 2, 3, 4, 5, 6, 7]
       Hit min-max/range/coverage: 0x02 - 0x07 (02₁₀ - 07₁₀) / 06₁₀ / 06₁₀.
  Expected min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
                    Covered range: 75.00%

preset calls:
       Hit min-max/range: 0x00 - 0xfe (00₁₀ - 254₁₀) / 255₁₀.
  Expected min-max/range: 0x00 - 0xfe (00₁₀ - 254₁₀) / 255₁₀.

Total PTZ coverage: 39.06%
```

See also:

* [Testing Approach](../Testing-Approach.md)
