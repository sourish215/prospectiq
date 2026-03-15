from app.db.supabase_client import supabase


def search_chunks(query_embedding):

    result = supabase.rpc(
        "match_chunks",
        {
            "query_embedding": query_embedding,
            "match_count": 5
        }
    ).execute()

    return result.data
