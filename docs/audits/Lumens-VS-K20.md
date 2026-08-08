# Lumens VS-K20

<https://www.mylumens.com/en/Products_detail/5/VS-K20>

## Observations

1. PTZ Controls:
	1. Pan: Limited to a contiguous and non-adjustable 13 speeds (0-12) of an expected 24.
	2. Tilt: Limited to a contiguous and non-adjustable 11 speeds (0-10) of an expected 24.
	3. ✅ Zoom: Provides a full range of all 8 zoom speeds.
	4. Overall coverage score: 50.00%.
2. No seesaw lever option for zoom control.
3. ⚠️ Focus control is tied into the zoom on the joystick, making it impossible to use the zoom control while in manual focus.

### Availability

Appears to be no longer available for sale as of August 2026, at least not within the US.
The [VS-KB21](https://www.mylumens.com/en/Products_detail/1117/VS-KB21-IP-Camera-Controller) may be the next best replacement from the same company.

### OLED Display

⚠️ The OLED display is prone to dimming and failure.
The display is a WiseChip <!-- cSpell:disable -->UG-2832GSWFG02<!-- cSpell:enable -->.
It looks like it should be easy enough to solder-in a replacement, but the display was discontinued by the manufacturer in 2022, and am unable to locate any replacements.

## Firmware Version Tested

Tested: 2026-08-01

## Raw Test Results

```text
visca_audit.py 2026-08-01

power on time:
  time: 4.65s

pan left:
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, _, _, _, _, _, _, _, _, _, _, _, _]
       Hit min-max/range/coverage: 0x00 - 0x0c (00₁₀ - 12₁₀) / 13₁₀ / 13₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 54.17%

pan right:
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, _, _, _, _, _, _, _, _, _, _, _, _]
       Hit min-max/range/coverage: 0x00 - 0x0c (00₁₀ - 12₁₀) / 13₁₀ / 13₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 54.17%

tilt up:
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, _, _, _, _, _, _, _, _, _, _, _, _, _, _]
       Hit min-max/range/coverage: 0x00 - 0x0a (00₁₀ - 10₁₀) / 11₁₀ / 11₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 45.83%

tilt down:
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, _, _, _, _, _, _, _, _, _, _, _, _, _, _]
       Hit min-max/range/coverage: 0x00 - 0x0a (00₁₀ - 10₁₀) / 11₁₀ / 11₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 45.83%

zoom tele seesaw:
  [_, _, _, _, _, _, _, _]
       Hit min-max/range/coverage: 0x   - 0x   (  ₁₀ -   ₁₀) / 00₁₀ / 00₁₀.
  Expected min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
                    Covered range: 0.00%

zoom wide seesaw:
  [_, _, _, _, _, _, _, _]
       Hit min-max/range/coverage: 0x   - 0x   (  ₁₀ -   ₁₀) / 00₁₀ / 00₁₀.
  Expected min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
                    Covered range: 0.00%

zoom tele joystick:
  [0, 1, 2, 3, 4, 5, 6, 7]
       Hit min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
  Expected min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
                    Covered range: 100.00%

zoom wide joystick:
  [0, 1, 2, 3, 4, 5, 6, 7]
       Hit min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
  Expected min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
                    Covered range: 100.00%

preset calls:
       Hit min-max/range: 0x00 - 0xfe (00₁₀ - 254₁₀) / 255₁₀.
  Expected min-max/range: 0x00 - 0xfe (00₁₀ - 254₁₀) / 255₁₀.

Total PTZ coverage: 50.00%
```

See also:

* [Testing Approach](../Testing-Approach.md)
