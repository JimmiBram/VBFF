import sqlite3

def create_connection(db_file):
    """Opret en databaseforbindelse til SQLite-databasen."""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

def view_all_artists(conn):
    """Vis alle kunstnere i databasen."""
    cursor = conn.cursor()
    cursor.execute("SELECT ArtistId, Name FROM Artist ORDER BY Name;")
    artists = cursor.fetchall()
    print("\nList of Artists:")
    for artist in artists:
        print(f"{artist[0]}: {artist[1]}")

def search_artist(conn):
    """Søg efter kunstnere efter navn."""
    search_term = input("\nEnter artist name to search: ").strip()
    cursor = conn.cursor()
    query = "SELECT ArtistId, Name FROM Artist WHERE Name LIKE ? ORDER BY Name;"
    cursor.execute(query, ('%' + search_term + '%',))
    results = cursor.fetchall()
    if results:
        print("\nSearch Results:")
        for artist in results:
            print(f"{artist[0]}: {artist[1]}")
    else:
        print("No artists found with that name.")

def view_albums_by_artist(conn):
    """Vis albums af en specifik kunstner."""
    artist_id = input("\nEnter the Artist ID to view their albums: ").strip()
    cursor = conn.cursor()
    query = "SELECT Title, AlbumId FROM Album WHERE ArtistId = ? ORDER BY Title;"
    cursor.execute(query, (artist_id,))
    albums = cursor.fetchall()
    if albums:
        print("\nAlbums:")
        for album in albums:
            print(f"{album[1]}: {album[0]}")
    else:
        print("No albums found for this artist.")

def view_tracks_in_album(conn):
    """Vis numre i et specifikt album."""
    album_id = input("\nEnter the Album ID to view its tracks: ").strip()
    cursor = conn.cursor()
    query = "SELECT Name, TrackId FROM Track WHERE AlbumId = ? ORDER BY Name;"
    cursor.execute(query, (album_id,))
    tracks = cursor.fetchall()
    if tracks:
        print("\nTracks:")
        for track in tracks:
            print(f"{track[1]}: {track[0]}")
    else:
        print("No tracks found for this album.")

def view_top_tracks(conn):
    """Vis de top 5 numre efter salg."""
    cursor = conn.cursor()
    query = """
    SELECT Track.Name, COUNT(InvoiceLine.InvoiceLineId) as Sales
    FROM Track
    JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId
    GROUP BY Track.TrackId
    ORDER BY Sales DESC
    LIMIT 5;
    """
    cursor.execute(query)
    top_tracks = cursor.fetchall()
    print("\nTop 5 Tracks by Sales:")
    for idx, track in enumerate(top_tracks, start=1):
        print(f"{idx}. {track[0]} - {track[1]} sales")

def main_menu(conn):
    """Vis hovedmenuen og håndter brugerinput."""
    while True:
        print("\n--- Welcome to Vordingborg Music Store ---")
        print("1. View All Artists")
        print("2. Search for an Artist")
        print("3. View Albums by an Artist")
        print("4. View Tracks in an Album")
        print("5. View Top 5 Tracks by Sales")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            view_all_artists(conn)
        elif choice == '2':
            search_artist(conn)
        elif choice == '3':
            view_albums_by_artist(conn)
        elif choice == '4':
            view_tracks_in_album(conn)
        elif choice == '5':
            view_top_tracks(conn)
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == '__main__':
    database = 'Chinook_Sqlite.sqlite'  # Opdater sti hvis nødvendigt
    conn = create_connection(database)
    
    if conn:
        main_menu(conn)
        conn.close()
    else:
        print("Error! Cannot connect to the database.")
