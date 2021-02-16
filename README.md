## US Accident Hotspots

This notebook does the following:

1. Imports US Traffic Accident data from 2016-2020 (<a href="https://www.kaggle.com/sobhanmoosavi/us-accidents">source</a>) 
2. Geocodes the accident lat/lon cooardinates to <a href="https://eng.uber.com/h3/">H3 Bins</a>
3. Clusters together H3 bins with close proximity to create accident "hotspots"
4. Calculates Metrics for each of those Regions
5. Visualize the hotspots within <a href="https://kepler.gl/">Kepler GL</a>

Shout out to <a href="https://github.com/kennethkuhn">@Kenneth_Kuhn</a> for assistance with the image_processing component! 

### Example of Map Output:
To explore the interactive map checkout US_Accident_Hotspots.html file

<img src="images/hotspots.png" alt="drawing" width="600"/>
