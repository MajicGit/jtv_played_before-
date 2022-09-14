# jtv_played_before
 Uses the ticket lists to get a list of videos that have been played on JungleTV.

Note that this list is in no way or form comprehensive. Errors can and will occur, additionally the ticket lists that this relies on don't date back to the initial creation of JungleTV. Thus be careful when relying on this for winning events or so. I take no guarantee for the correctness. 

## To run yourself:

1. (Optional) Create a file called "config.py". In this you need to specify your Youtube Data v3 API  as `api_key = "YOUR_API_KEY"`. Optionally you can also adjust the `MIN_PLAYS_FOR_LOOKUP` [value in this file](./jtv_lists.py), to change how many videos names are resolved. 
2. Run `python3 jtv_lists.py` and wait.
