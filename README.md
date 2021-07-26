# Pop to Click

Talon has exactly two noises that are built in and immediately recognizeable.  (You can add more, but the setup is a lot more intensive, and I bet you'd rather get started as quickly as possible. 

Demonstration of what the popping sound is supposed to sound like: 

https://www.youtube.com/watch?v=VMNsU7rrjRI


instructions for making the popping noise, as found on noise.talonvoice.com: 

```
Making The Sound
- Relax your jaw and keep your lips pressed very gently together
- Push a very tiny bit of air into your mouth, then quickly open your jaw, pulling your lips apart
- This should create a gentle pop sound that resonates within your mouth and cheeks
- This works best with a bit of moisture on your lips
- Not everyone can do this!
```


This file allows you to save your index finger a lot of clicking by replacing the physical motion of clicking a mouse, tapping a touchpad, or tapping a screen, wth making a popping noise with your mouth.  

Assuming the following:

1. You have followed the setup instructions for [talon](talonvoice.net), and have successfully set up all three componets for a talon insall (Talon itself, the voice engine, and a scripting set). 
2. The pop noise is not being used for anything else in the scripting set you have installed. (for example, you are not using the default knausj_master scripting set, and don't have an eye-tracker that is currently using ctrl_mouse_mode)
3. Place the pop_to_click folder with the pop_to_click.py file anywhere in the talon user directory.  The talon user directory is accessible from the talon menu or from the command line at ~/talon/user on macOSx and linux or %APPDATA%\Talon\user in the Windows file explorer on Windows.

4. Then, when you make a popping noise with your mouth, your mouse cursor will click on whatever you are pointing to at the time. if you double-pop, it is fast enough register as a double-click, and if you are fast enough with the noise you can even convice it to triple-click.  


