import re
import requests

def extract_ids_from_lua(file_path):
    ids = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r'resource\.AddWorkshop\("(\d+)"\)', line)
            if match:
                ids.append(match.group(1))
    return ids

def fetch_ids_from_collection(api_key, collection_id):
    url = "https://api.steampowered.com/ISteamRemoteStorage/GetCollectionDetails/v1/"
    payload = {
        'collectioncount': 1,
        'publishedfileids[0]': collection_id
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    data = response.json()
    children = data['response']['collectiondetails'][0].get('children', [])
    return [child['publishedfileid'] for child in children if child['filetype'] == 0]

def compare_ids(lua_ids, collection_ids):
    missing_in_lua = list(set(collection_ids) - set(lua_ids))
    extra_in_lua = list(set(lua_ids) - set(collection_ids))
    return missing_in_lua, extra_in_lua

def main():
    lua_path = input("📄 Path to collection.lua: ").strip()
    collection_id = input("📦 Workshop Collection ID: ").strip()
    api_key = input("🔑 Steam Web API Key: ").strip()

    try:
        lua_ids = extract_ids_from_lua(lua_path)
        collection_ids = fetch_ids_from_collection(api_key, collection_id)

        missing, extra = compare_ids(lua_ids, collection_ids)

        print("\n=== Comparison Report ===")
        if missing:
            print(f"\n🚫 Missing in Lua ({len(missing)}):")
            for mid in missing:
                print(f"- {mid}")

        if extra:
            print(f"\n⚠️ Extra in Lua (not in collection) ({len(extra)}):")
            for eid in extra:
                print(f"- {eid}")

        if not missing and not extra:
            print("\n✅ Everything is synced!")

    except Exception as e:
        print(f"[❌] Error: {e}")

if __name__ == "__main__":
    main()
