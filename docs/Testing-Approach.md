# Testing Approach

Tests are executed using [`visca_audit.py`](../src/visca_audit/visca_audit.py).

See also: [README.md](../README.md).

## Pan / Tilt / Zoom

1. Ensure all speed controls are set to 100% (not limited / scaled).
	1. Reducing the associated speed dials / knobs / controls may yield additional speed levels due to scaling, but only speed levels signaled when the speed knobs are set to 100% are to be included in the test results.
2. Slowly exercise the controls to the full extent.
	1. Repeat continuously, attempting to focus the speeds to and around any potentially missing speed levels that have not yet been detected.
3. Testing is performed over VISCA Serial RS-232 only.

PTZ Coverage represents the percentage of the VISCA PTZ speed parameter combinations that the tested controller can directly select and transmit.

### Sample Results

#### ⚠️ Substandard Result

1. Only 8 of the expected 24 speeds are covered.
	1. This results in noticeable jumps / skips between speeds, instead of having the desired fluid acceleration / deceleration.
2. The first 2 speeds (1 - 2) are missing.
	1. These missing lowest speeds are useful for minor positioning adjustments of the camera, without jump-starting at a higher speed - or without first needing to throttle the speed control using a separate knob control.

```text
       Hit min-max/range: 0x03 - 0x18 (03₁₀ - 24₁₀) / 22₁₀.
  Expected min-max/range: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀.
  [_, _, _, 3, _, _, 6, _, _, 9, _, _, 12, _, _, 15, _, _, 18, _, _, 21, _, _, 24]
       Hit min-max/range/coverage: 0x03 - 0x18 (03₁₀ - 24₁₀) / 22₁₀ / 08₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 33.33%
```

I.E., only a limited range of control speeds are covered, and only at limited resolution.

#### ✅ Ideal Result

1. All 24 of the expected 24 speeds are covered.
2. No speeds are missing.

```text
       Hit min-max/range: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀.
  Expected min-max/range: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀.
  [_, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
       Hit min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 100.00%
```

I.E., the full range of control speeds are covered, and at full resolution.
