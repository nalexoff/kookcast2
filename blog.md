this prompt worked after i figured out the curl with help from chatgpt:

"""

convert this curl command into python, however make it so that the start and end date parameters provided always reflect the current day: curl -H "token: LeRhYpFmZmwpAzFDJicsMqEntqNgiCqU" "https://www.ncei.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&stationid=GHCND:USW00014719&startdate=2023-03-20&enddate=2023-03-20&limit=1000"

"""

not that surprising, it's pretty explicit. it helped i verified the request first via the terminal. broader requests ended up with code that was a bit too compelx for what i needed

 notes on first interactions
- setting up an ide is a bit of a pain, i can see why something like replit is attractive to get going quickly. it may be more attractive with more complex projects w/ multiple languages?
- having autopilot suggest additional items on the 'todo' list/shape the problem was a cool little surprise.
- ultimately having a separate window up with chatgpt was useful...i felt more comfortable with broader questions there, and the back-and-forth was useful. i'm not sure i'm at the level or place where autopilot's 'comment to code' functionality was useful for me. i think their featureset in autopilot x will probably correct that - i signed up for the waitlist
- chatgpt was useful in navigating api documentation for me … 'what data types are available here, what datasets are avialable, etc.' 
- prompts matter a lot … when i was overly broad i got working code but not useful for where i was at … smaller and more specific was better and allowed me to make progress
- pumping errors back into chatgpt and having it fix code worked surprisingly well … there's a bit of brute forcing involved but if you've got a kernel of something working, you can probably copy and paste your way into a working solution (im sure this doesn't scale well)
- got overly excited to turn things over to the computer and ultimately wasted time getting something working, but that's of little value for what i want to do. if i slowed down in the beginning and read the published docs a bit more, I would've realized (1) the information i was looking for was easily accessible through a UI that was provided and (2) the refresh rate of the data doesn't really meet the needs of my use case. feels like the classic error of rushing towards a solution…
- API discovery with chatgpt worked pretty well … i knew the data I wanted, but not what API might provide it. It was very much like googling, but more specific and I think useful. 
