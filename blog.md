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

second interaction
- separate from coding with these tools, chatgpt was able to parse the text of a forecast provided by the NDBC and actually provide me with a greater understanding of it then i had previously. this makes me think that while extracting this text in a programmatic way will be useful, what will be even better will be to feed it to chatgpt and ask for analysis of it. i should look into the gpt api and figure out how to feed it my lists of forecast information and get a summary response.
- in general i'm not using autopilot at all, chatgpt is writing the code for me. i'm just copy and pasting. if i'm not leveraging prior experience (ie, i should write a function for this, create a class for this, etc.) and starting to initiate the writing of the code myself, then autopilot has little use for me
- i used 3.5 to get a working solution, then asked gpt4 for suggestions on how to improve the code. it did seem to produce a more 'maintainable' solution, but at the same time it introduced a bug that 3.5 didn't have. we eventually got it working again, but i'm a little uneasy about not understanding the situation – will the fix work in all cases? i'm not sure. 
- i still had to validate solutions quite a bit. for example one attempt at the bug fix worked for the original bug, but introduced a new one in the process 
- 

third interaction
- adding some edge case handling in and the solution from gpt-4 was to handle the edge case outside of the function. this surprised me a bit and i asked it to incorporate a working solution within a function itself. it complied but i don't have any intuition whether this was a good idea or not. I wish it could identify when one of my suggestions is a bad one. feeding the code back to it and asking for improvements may net a change, or not. 
- it's a bit surreal to set chatgpt off on a task and go handle something else in the meantime. it does feel like an assistant/employee that you can delegate tasks to.
- 