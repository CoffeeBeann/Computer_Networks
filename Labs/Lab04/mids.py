# Filename: Mids.py
# Author: Ian Coffey (m261194)
# To Frontend Query Schedule in Mids

# Import Libraries
import requests

# Request Alpha
alpha = input("Enter Alpha: ")

# URL
url = "https://mids.usna.edu/ITSD/mids/drgwq010$mids.actionquery"

# Form
header = { 
    
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding" : "gzip, deflate, br, zstd",
    "accept-language" : "en-US,en;q=0.9",
    "cache-control" : "max-age=0",
    "connection" : "keep-alive",
    "content-type" : "application/x-www-form-urlencoded",
    "cookie" : "memory_sched_P_SECT_ID_IN=; memory_sched_P_BLOCKED_PERIODS_IN=; memory_sched_state=Saved; memory_sched_P_COUR_ID_IN=28%20254%20255%20277%20280%20340%20; memory_sched_P_EXCLUDE_FULL_SECTIONS_IN=true; f5_cspm=1234; WSG$DMJWQ002$URL0=/ITSD/mids/dmjwq002$.startup; WSG$DMJWQ002$CAP0=Matrices_-_Query_Current_Midshipman; WSG$DRGWQ010$URL0=/ITSD/mids/drgwq010$.startup; WSG$DRGWQ010$CAP0=Schedules_-_Query_Midshipmen; AMP_MKTG_075dfa7287=JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRm5pbWl0endlYnByaW50LnVzbmEuZWR1JTNBOTE5MiUyRnVzZXIlMkYlMjIlMkMlMjJyZWZlcnJpbmdfZG9tYWluJTIyJTNBJTIybmltaXR6d2VicHJpbnQudXNuYS5lZHUlM0E5MTkyJTIyJTdE; AMP_075dfa7287=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI4NDY0MmI5Ni00NmIzLTRhYTItYTFkZS1jZjFhNGQxOTFlMTElMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzA3MzMxNDMyNTg3JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcwNzMzMTQ2MTg1MyU3RA==; nmstat=2a4aade1-a102-8a39-b5e6-91a8a6601a87; _gid=GA1.2.2146473901.1726665909; _ga=GA1.2.1345064742.1666191482; _ga_LY79N0FLBS=GS1.1.1726680282.477.0.1726680282.0.0.0; BIGipServermids_prod=!bejSoCW1NeCyjlBHrP/1DhKiDM7x/jlXLvWKOBcUOxcZZBQX8mCu2Wj1iatC8hY/eBgUMZ13JVSL9g==; f5avraaaaaaaaaaaaaaaa_session_=NMKMODIPKLNBMKNENIDOGCHMMFIJBHMHBEECHAFAEFMEPDBAEEJLOFKHDDAAOMLLJLJDMNPHDADDNHCOAKAAKBAHLGOPDLODJNLBOABCGOGFBIKIBJAAOLHCOHCNENHB; OAMAuthnCookie_mids.usna.edu:443=pG%2FuOowrVWDC7JXPfCrjJim1FMJttL6mMoHSlX6p%2FTY172XYXI1V6lFDqa5AtFWacPMxfADGS7jtqoujZBwJ6FO%2BWaRDkTlt5VfUCg1Vc2xYhF%2FfumHIi8Odd%2BsqYmDDmOTgdd2%2F8eccQb4ZW5EkVRDsPhM7P2Lrz876N7qGR%2BhQ2ToCqm5OD0LXAxji9JM6MyLTRPK%2Bz3l7JVWqLwH3GRzZw45ZwtrXFBIW7Pv%2FaQyqsBPun88SafRXyJrKWbhyVJWw5S6mGwnLyIA9GkiylQtUXbhdsuRxtzFL5hjdU7qUrxSj3wKpGFV4%2B91iI%2FiOKrLypDZTcHdyksgbf9m1y4OUGP8aBYEw6X7Cvgh%2BQAmadOaZ8m8sl4VWSE02eDb9nvjACI8kEbbf9SBev%2FrPCLQK%2F3h5ibMaAb3%2FDh8xTjkF6vXrZ4XW3CtfRw9o503FO4P7QKRjyLls4wG8%2FIZks2P3MVNXvrfW29XVoWgvAPkN445dpPAU6P0sjhQHG80Sac%2BjBY%2Flr7Q6gqWg9sGRQL04CjXXSXMwVm6z3R2HIiPEgmq83TLxGZIgxEeNBhBdzdUKlpCA2Apdz%2FnpLSBFBQ%3D%3D",
    "host" : "mids.usna.edu",
    "origin" : "https://mids.usna.edu",
    "referer" : "https://mids.usna.edu/ITSD/mids/drgwq010$.startup",
    "sec-ch-ua-mobile" : "?0",
    "sec-ch-ua-platform" : "Windows",
    "sec-fetch-dest" : "document",
    "sec-fetch-mode" : "navigate",
    "sec-fetch-site" : "same-origin",
    "sec-fetch-user" : "?1",
    "upgrade-insecure-requests" : "1",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
}

# Payload
payload = {
    "P_ALPHA" : f"{alpha}",
    "P_SECOF_COOF_SEBLDA_AC_YR" : "2025",
    "P_SECOF_COOF_SEBLDA_SEM" : "FALL",
    "P_SECOF_COOF_SEBLDA_BLK_NBR" : "1",
    "Z_ACTION" : "QUERY",
    "Z_CHK" : "0",
}

# Create response
response = requests.post(url, data=payload, headers=header, verify=False)

# Output response to html
file = open('output.html', "w")
file.write(response.text)

