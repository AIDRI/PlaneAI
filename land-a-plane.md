Warning: this project is an AI project, but remember that AI is based on math.  
It is therefore allowed to create a project based only on math, or with a part of
AI, etc...  

Second part docs:  
- This second part is dedicated to the landing of the plane.  The plane must be able to detect the runway, to be able to land smoothly. We will assume that the aircraft's existing autopilot has helped to focus the aircraft on the correct approach. So we will have to manage a 3D airspace to be able to move the plane, correct the trajectory, and bring it down, keeping a speed of 110mph for our test plane, with a margin of error of 10mph. Be careful, the goal is to keep the margin of error as small as possible. After detecting the runway, we will have access to our altitude minus the altitude of the airport. We will therefore adjust our altitude to land on the runway. This part is relatively simple, but the goal is to detect the runway as far as possible to have the smoothest possible descent.
