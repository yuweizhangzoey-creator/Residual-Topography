import numpy as np
import geopandas as gpd
import pandas as pd

def define_profiles(path,nsteps):

    subductions=gpd.read_file(path)

    n_segs = len(subductions['Lon'])
    n_steps = nsteps
    dres = 0.1
    lats = np.zeros((n_steps, n_segs))
    lons = np.zeros((n_steps, n_segs))

    Profiles=[]
    Distances = []
    distance = 0
    R=6371  
    ilon = subductions['Lon']
    ilat = subductions['Lat']

    for i in range(1, n_steps):
        dlon = dres*np.sin(np.radians(subductions['Trench Normal Angle']))
        dlat = dres*np.cos(np.radians(subductions['Trench Normal Angle']))

        ilon = ilon + dlon
        ilat = ilat + dlat

        dlat_km = np.radians(dlat)*R
        dlon_km = np.radians(dlon)*R*np.cos(np.radians(ilat))
        distance = distance + np.sqrt(dlat_km**2 + dlon_km**2)

        profile=[f"Profile {j}" for j in range(0,len(ilon))]
    
        lats[i]=ilat
        lons[i]=ilon
        Distances.append(distance)
        Profiles.append(profile)

    lons=lons[1:].reshape(-1)
    lats=lats[1:].reshape(-1)
    Distances = [item for sublist in Distances for item in sublist]
    Profiles = [item for sublist in Profiles for item in sublist]
    profile_df=pd.DataFrame({'Longitude':lons,'Latitude':lats,'Distance': Distances, "Profile Name": Profiles})

    
    profile=[]
    for i in range(0, n_segs):
        profile_i= profile_df[profile_df['Profile Name']==f"Profile {i}"]


        profile.append(profile_i)
    


    return profile

def filter_by_extent(df, min_lon, max_lon, min_lat, max_lat):
    # Convert negative longitudes (e.g., -150) to 0–360 system
    df = df.copy()
    df.loc[df['Lon'] < 0, 'Lon'] = df['Lon'] + 360

    # Filter by extent
    filtered = df[
        (df['Lon'] >= min_lon) & (df['Lon'] <= max_lon) &
        (df['Lat'] >= min_lat) & (df['Lat'] <= max_lat)
    ]
    return filtered

