from telegraph import TelegraphAPI

def main():
    telegraph_api = TelegraphAPI()

    print("Testing createAccount...")
    account = telegraph_api.create_account(short_name="TestUser", author_name="Anonymous", author_url="https://example.com")
    print(f"Account created: {account}")
    
    access_token = account['access_token']
    telegraph_api = TelegraphAPI(access_token)

    print("Testing getAccountInfo...")
    account_info = telegraph_api.get_account_info()
    print(f"Account info: {account_info}")
    
    print("Testing editAccountInfo...")
    updated_account = telegraph_api.edit_account_info(short_name="NewTestUser", author_name="UpdatedAuthor")
    print(f"Account updated: {updated_account}")

    print("Testing createPage...")
    content = [{"tag": "p", "children": ["Hello, this is a sample page."]}]
    page = telegraph_api.create_page(title="Sample Page", content=content, author_name="Anonymous", return_content=True)
    print(f"Page created: {page}")

    print("Testing getPage...")
    page_path = page['path']
    fetched_page = telegraph_api.get_page(page_path, return_content=True)
    print(f"Fetched page: {fetched_page}")

    print("Testing getPageList...")
    page_list = telegraph_api.get_page_list(limit=5)
    print(f"Page list: {page_list}")

    print("Testing getViews...")
    page_views = telegraph_api.get_views(page_path)
    print(f"Page views: {page_views}")

    print("Testing revokeAccessToken...")
    revoked_account = telegraph_api.revoke_access_token()
    print(f"Access token revoked, new account info: {revoked_account}")

if __name__ == "__main__":
    main()