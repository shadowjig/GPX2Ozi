# GPX2Ozi
App to convert waypoint file from GPX to OziExplorer format.  I geocache and I wanted. I wanted to be able to capture GPX waypoints and upload them to my GPS without using a computer. Using cgeo (for browsing caches and exporting the GPX file) and GPSDump (for uploading the waypoints). Only problem was the GPSDump doesn't support GPX imports yet. So I created this Kivy app.
 
This app uses Kivy and Python, so it can run on Windows, Android, OSX or IOS.  The only additional code I used was a GPX reader called gpxpy (https://github.com/tkrajina/gpxpy).

To use this app you can grab the source and gpxpy and run it on your phone using the Kivy Launcher (see Kivy docs).  Or you can download the Android apk in the bin directory.  It's signed so it should install without an issue.

I don't have any Apple machines or IOS devices, but you should be able to read the Kivy docs and compile this code to a IOS package.
