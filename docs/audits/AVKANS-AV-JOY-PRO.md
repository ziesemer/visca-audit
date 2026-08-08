# AVKANS AV-JOY-PRO

<https://avkans.com/products/avkans-pro-ptz-camera-joystick-controller-with-5-inch-touch-preview-lcd-ip-ndi-camera-controller-keyboard-with-4d-joystick-for-worship-church-live-streaming-video-production-poe-enable-5-inch-touch-screen>

## Observations

1. PTZ Controls:
	1. Pan & Tilt: Limited to 20 levels of speed in any direction of an expected 24.
		1. Range of those speeds are configurable by using the speed dial.
	2. Zoom: Limited to 5-7 levels of speed in either direction (depending upon which control used) of an expected 8.
		1. Range of those speeds are configurable by using the speed dial.
	3. Overall coverage score: 82.03%.
		1. While not 100%, this is the highest score of all products tested in the catalog here (as of 2026-08-03).
2. ⚠️ Camera Preset 0 is not usable.
3. ✅ Has "Quick Call" feature for presets.
	1. ⚠️ As Camera Preset 0 is not usable (above), the "0" key here is also wasted and unusable for Quick Call.
4. ⚠️ The "Backlight" and "Key Brightness" settings are troublesome.
	Neither appears to save after a reboot.
	1. Then even at least sometimes, after setting the "Key Brightness" to 2, the keys are actually lit at 10 - until changing to a non-2 value and then back to 2 again.
5. ⚠️ Cannot find documentation or explanation for what the difference is for configuring the camera "Mode" between "Normal 1" and "Visca 2".
6. ⚠️ When switching between cameras and the controller tries to read the current settings from the prior camera, the "Auto Focus" indicator does not re-illuminate upon connection, even though Auto Focus is turned on, and the cameras reply as such (confirmed with a signal capture).
	1. Camera 1 works as expected, but Camera 2 and Camera 3 both exhibit this.
	2. I was able to reproduce this from a simulation ([`visca_responder.py`](../../src/visca_audit/visca_responder.py)) that sends identical responses regardless of camera address.
7. ⚠️ Switching delay between cameras - it currently takes about 1.2 seconds to switch from camera to camera.
	1. Interestingly, each camera switch begins with sending 3 "stop" commands first to the prior camera (focus, zoom, P/T).
		The controller should know which commands are in-progress, if any, and spend the time only cancelling those that may still be in-progress (having received no prior completion or error responses for).
		This takes about 0.3 seconds.
		1. ⚠️ This also comes with the consequence of potentially stopping in-flight commands from another controller, which should not be aborted.
	2. The controller also waits about 0.8 seconds, then sends 2 "Tally Mode - Lights Off" commands.
		1. The current manual, on page 13, indicates that the "PGM Signal" should be able to select "OFF, PGM In or PGM Out".
			It seems like "Off" would be ideal here, but I only have options for "Out" and "In".
			In the menu under "Custom / Other", I also have a few other settings that are not in the manual.
			One of those is "Cam Tally", with options of "Off", "Low", and "High" - though this is already set to "Off".
	3. Also maybe an option to not query the camera at all upon selection, and just remember the prior settings per-camera.
		(This would have to assume that the controller is the only controller controlling the cameras.)

This has a chance to be a *fantastic* controller, with what should hopefully be a few fast and easy firmware updates.

### Support

Support has been very responsive, though still waiting for any firmware updates for reported issues and findings.

## Related Hardware

This hardware appears to be identical to:

* AV Matrix PKC4000: <https://www.avmatrix.com/products/pkc4000-ip-serial-ptz-camera-controller/>
* Lilliput K2: <https://lilliputweb.net/k2/>

Uncertain as to differences in firmware, revisions in hardware, etc., across these products.

## Firmware Version Tested

Tested: 2026-08-01

| | Version |
| --- | --: |
| Software / APP | V1.3.134-A |
| MCU | V1.5 |

## Raw Test Results

```text
visca_audit.py 2026-08-01

power on time:
  time: 10.62s

pan left:
       Hit min-max/range: 0x05 - 0x18 (05₁₀ - 24₁₀) / 20₁₀.
  Expected min-max/range: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀.
  [_, _, _, _, _, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
       Hit min-max/range/coverage: 0x05 - 0x18 (05₁₀ - 24₁₀) / 20₁₀ / 20₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 83.33%

pan right:
       Hit min-max/range: 0x05 - 0x18 (05₁₀ - 24₁₀) / 20₁₀.
  Expected min-max/range: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀.
  [_, _, _, _, _, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
       Hit min-max/range/coverage: 0x05 - 0x18 (05₁₀ - 24₁₀) / 20₁₀ / 20₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 83.33%

tilt up:
       Hit min-max/range: 0x05 - 0x18 (05₁₀ - 24₁₀) / 20₁₀.
  Expected min-max/range: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀.
  [_, _, _, _, _, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
       Hit min-max/range/coverage: 0x05 - 0x18 (05₁₀ - 24₁₀) / 20₁₀ / 20₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 83.33%

tilt down:
       Hit min-max/range: 0x05 - 0x18 (05₁₀ - 24₁₀) / 20₁₀.
  Expected min-max/range: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀.
  [_, _, _, _, _, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
       Hit min-max/range/coverage: 0x05 - 0x18 (05₁₀ - 24₁₀) / 20₁₀ / 20₁₀.
  Expected min-max/range/coverage: 0x01 - 0x18 (01₁₀ - 24₁₀) / 24₁₀ / 24₁₀.
                    Covered range: 83.33%

zoom tele seesaw:
       Hit min-max/range: 0x02 - 0x07 (02₁₀ - 07₁₀) / 06₁₀.
  Expected min-max/range: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀.
  [_, _, 2, 3, 4, 5, 6, 7]
       Hit min-max/range/coverage: 0x02 - 0x07 (02₁₀ - 07₁₀) / 06₁₀ / 06₁₀.
  Expected min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
                    Covered range: 75.00%

zoom wide seesaw:
       Hit min-max/range: 0x02 - 0x06 (02₁₀ - 06₁₀) / 05₁₀.
  Expected min-max/range: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀.
  [_, _, 2, 3, 4, 5, 6, _]
       Hit min-max/range/coverage: 0x02 - 0x06 (02₁₀ - 06₁₀) / 05₁₀ / 05₁₀.
  Expected min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
                    Covered range: 62.50%

zoom tele joystick:
       Hit min-max/range: 0x01 - 0x07 (01₁₀ - 07₁₀) / 07₁₀.
  Expected min-max/range: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀.
  [_, 1, 2, 3, 4, 5, 6, 7]
       Hit min-max/range/coverage: 0x01 - 0x07 (01₁₀ - 07₁₀) / 07₁₀ / 07₁₀.
  Expected min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
                    Covered range: 87.50%

zoom wide joystick:
       Hit min-max/range: 0x01 - 0x07 (01₁₀ - 07₁₀) / 07₁₀.
  Expected min-max/range: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀.
  [_, 1, 2, 3, 4, 5, 6, 7]
       Hit min-max/range/coverage: 0x01 - 0x07 (01₁₀ - 07₁₀) / 07₁₀ / 07₁₀.
  Expected min-max/range/coverage: 0x00 - 0x07 (00₁₀ - 07₁₀) / 08₁₀ / 08₁₀.
                    Covered range: 87.50%

preset calls:
       Hit min-max/range: 0x01 - 0xfe (01₁₀ - 254₁₀) / 254₁₀.
  Expected min-max/range: 0x00 - 0xfe (00₁₀ - 254₁₀) / 255₁₀.

Total PTZ coverage: 82.03%
```

See also:

* [Testing Approach](../Testing-Approach.md)
