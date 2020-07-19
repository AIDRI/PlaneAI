Warning: this project is an AI project, but remember that AI is based on math.  
It is therefore allowed to create a project based only on math, or with a part of
AI, etc...  

Third part docs:  
- This part is relatively simple to understand, the principle is to detect the yellow lines
on the runway and then follow them to an aircraft parking spot.  
Note that the runways have a white line in the centre of the runway, from which the various
yellow lines that we'll call taxiways.
In many ways, this project resembles a self-driving car project.
However, no simulator allows us to have a plane with the necessary equipment, 
such as lidar, radar, gmu, gnss, and satellites, we'll be relying on a camera that
will be attached to the pilot's view (or the centre of the aircraft, as desired). To avoid collisions
between planes, we're going to pretend to have a system to guide the planes...
on taxiways, which is the first part of the project.  
For this project, we will use the runways and taxiways of the airport as a model.
Saint Exupéry in Lyon: https://www.google.com/url?sa=i&url=https%3A%2F%2Fthreadreaderapp.com%2Fthread%2F1057011706394800129.html&psig=AOvVaw33q0zKIjKbWP4hb-mjaOcV&ust=1595237457593000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJiAlOKA2eoCFQAAAAAdAAAAABA2  

The test aircraft will be a Cesna 172: here is a sheet with these useful characteristics:  
Length: 8.28 meters  
Wingspan: 11 m  
Height: 2.72 m  
Wing area: 16.2 m2  
Unladen mass: 744 kg  
Payload: 415 kg  
Maximum take-off weight: 1.157 kg  
Gravity of the airport: 9.81 m/s^2  

This data can be useful for moving the aircraft by using, for example, the formulas for the
dynamic modeling.  
