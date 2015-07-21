# GPX2Ozi
App to convert waypoint file from GPX to OziExplorer format.  I geocache and I wanted to be able to capture GPX waypoints and upload them to my GPS without using a computer.  Using cgeo (for browsing caches and exporing the GPX file) and GPSDump (from the play store for uploading the waypoints).  Only problem was the GPSDUMP doesn't support GPX imports yet.  So I created this Kivy app.

This app uses Kivy and Python, so it can run on Windows, Android, OSX or IOS.  The only additional code I used was a GPX reader called gpxpy (https://github.com/tkrajina/gpxpy).

To use this app you can download the Kivy Launcher, grab the source and gpxpy and it to your phone.  Run the source using the Kivy Launcher (see Kivy docs).  OR you can download the Android apk in the bin directory.  It's signed so it should install without and issue.

I don't have any Apple machines or IOS devices, but you should be able to read the Kivy docs and compile this code to a IOS package.
