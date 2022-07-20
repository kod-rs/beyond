import json

from keycloak import KeycloakOpenID

KEYCLOAK_CONFIG = {
    'KEYCLOAK_SERVER_URL': 'http://localhost:8080/auth',
    'KEYCLOAK_REALM': 'beyond_realm',
    'KEYCLOAK_CLIENT_ID': 'Myclient',
    'KEYCLOAK_CLIENT_SECRET_KEY': 'yMd5cnrqljbDwkBFlPNETyvhZPuNNf2e'
}
from keycloak import KeycloakAdmin

# Configure client
keycloak_openid = KeycloakOpenID(
    server_url=KEYCLOAK_CONFIG['KEYCLOAK_SERVER_URL'],
    client_id=KEYCLOAK_CONFIG["KEYCLOAK_CLIENT_ID"],
    realm_name=KEYCLOAK_CONFIG["KEYCLOAK_REALM"],
    client_secret_key=KEYCLOAK_CONFIG["KEYCLOAK_CLIENT_SECRET_KEY"]
                 )

keycloak_admin = KeycloakAdmin(
    username='useradmin',
       password='p',
    server_url=KEYCLOAK_CONFIG['KEYCLOAK_SERVER_URL'],

    realm_name=KEYCLOAK_CONFIG["KEYCLOAK_REALM"],
    # user_realm_name="only_if_other_realm_than_master",
    client_secret_key=KEYCLOAK_CONFIG["KEYCLOAK_CLIENT_SECRET_KEY"],
    verify=True)

# Add user
new_user = keycloak_admin.create_user({"email": "example@example.com",
                                       "username": "example@example.com",
                                       "enabled": True,
                                       "firstName": "Example",
                                       "lastName": "Example"})


# config_well_known = keycloak_openid.well_known()
# print(config_well_known)
#
# print(json.dumps(config_well_known, indent=4, sort_keys=True))

# access_token = keycloak_openid.token(
#     grant_type='authorization_code',
#     code='the_code_you_get_from_auth_url_callback',
#     redirect_uri="your_call_back_url")
#
# print(access_token)

def all_func():

    # Get WellKnow
    config_well_known = keycloak_openid.well_known()

    # Get Code With Oauth Authorization Request
    auth_url = keycloak_openid.auth_url(
        redirect_uri="your_call_back_url",
        scope="email",
        state="your_state_info")

    # Get Access Token With Code
    access_token = keycloak_openid.token(
        grant_type='authorization_code',
        code='the_code_you_get_from_auth_url_callback',
        redirect_uri="your_call_back_url")


    # Get Token
    token = keycloak_openid.token("user", "password")
    token = keycloak_openid.token("user", "password", totp="012345")

    # Get token using Token Exchange
    token = keycloak_openid.exchange_token(token['access_token'], "my_client", "other_client", "some_user")

    # Get Userinfo
    userinfo = keycloak_openid.userinfo(token['access_token'])

    # Refresh token
    token = keycloak_openid.refresh_token(token['refresh_token'])

    # Logout
    keycloak_openid.logout(token['refresh_token'])

    # Get Certs
    certs = keycloak_openid.certs()

    # Get RPT (Entitlement)
    token = keycloak_openid.token("user", "password")
    rpt = keycloak_openid.entitlement(token['access_token'], "resource_id")

    # Instropect RPT
    token_rpt_info = keycloak_openid.introspect(keycloak_openid.introspect(token['access_token'], rpt=rpt['rpt'],
                                         token_type_hint="requesting_party_token"))

    # Introspect Token
    token_info = keycloak_openid.introspect(token['access_token'])

    # Decode Token
    KEYCLOAK_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n" + keycloak_openid.public_key() + "\n-----END PUBLIC KEY-----"
    options = {"verify_signature": True, "verify_aud": True, "verify_exp": True}
    token_info = keycloak_openid.decode_token(token['access_token'], key=KEYCLOAK_PUBLIC_KEY, options=options)

    # Get permissions by token
    token = keycloak_openid.token("user", "password")
    keycloak_openid.load_authorization_config("example-authz-config.json")
    policies = keycloak_openid.get_policies(token['access_token'], method_token_info='decode', key=KEYCLOAK_PUBLIC_KEY)
    permissions = keycloak_openid.get_permissions(token['access_token'], method_token_info='introspect')

    # Get UMA-permissions by token
    token = keycloak_openid.token("user", "password")
    permissions = keycloak_openid.uma_permissions(token['access_token'])

    # Get UMA-permissions by token with specific resource and scope requested
    token = keycloak_openid.token("user", "password")
    permissions = keycloak_openid.uma_permissions(token['access_token'], permissions="Resource#Scope")

    # Get auth status for a specific resource and scope by token
    token = keycloak_openid.token("user", "password")
    auth_status = keycloak_openid.has_uma_access(token['access_token'], "Resource#Scope")

def admin_func():


    # Add user
    new_user = keycloak_admin.create_user({"email": "example@example.com",
                                           "username": "example@example.com",
                                           "enabled": True,
                                           "firstName": "Example",
                                           "lastName": "Example"})

    # Add user and raise exception if username already exists
    # exist_ok currently defaults to True for backwards compatibility reasons
    new_user = keycloak_admin.create_user({"email": "example@example.com",
                                           "username": "example@example.com",
                                           "enabled": True,
                                           "firstName": "Example",
                                           "lastName": "Example"},
                                          exist_ok=False)

    # Add user and set password
    new_user = keycloak_admin.create_user({"email": "example@example.com",
                                           "username": "example@example.com",
                                           "enabled": True,
                                           "firstName": "Example",
                                           "lastName": "Example",
                                           "credentials": [{"value": "secret",
                                                            "type": "password", }]})

    # Add user and specify a locale
    new_user = keycloak_admin.create_user({"email": "example@example.fr",
                                           "username": "example@example.fr",
                                           "enabled": True,
                                           "firstName": "Example",
                                           "lastName": "Example",
                                           "attributes": {
                                               "locale": ["fr"]
                                           }})

    # User counter
    count_users = keycloak_admin.users_count()

    # Get users Returns a list of users, filtered according to query parameters
    users = keycloak_admin.get_users({})

    # Get user ID from name
    user_id_keycloak = keycloak_admin.get_user_id("example@example.com")

    # Get User
    user = keycloak_admin.get_user("user-id-keycloak")

    # Update User
    response = keycloak_admin.update_user(user_id="user-id-keycloak",
                                          payload={
                                              'firstName': 'Example Update'})

    # Update User Password
    response = keycloak_admin.set_user_password(user_id="user-id-keycloak",
                                                password="secret",
                                                temporary=True)

    # Get User Credentials
    credentials = keycloak_admin.get_credentials(user_id='user_id')

    # Get User Credential by ID
    credential = keycloak_admin.get_credential(user_id='user_id',
                                               credential_id='credential_id')

    # Delete User Credential
    response = keycloak_admin.delete_credential(user_id='user_id',
                                                credential_id='credential_id')

    # Delete User
    response = keycloak_admin.delete_user(user_id="user-id-keycloak")

    # Get consents granted by the user
    consents = keycloak_admin.consents_user(user_id="user-id-keycloak")

    # Send User Action
    response = keycloak_admin.send_update_account(user_id="user-id-keycloak",
                                                  payload=json.dumps(
                                                      ['UPDATE_PASSWORD']))

    # Send Verify Email
    response = keycloak_admin.send_verify_email(user_id="user-id-keycloak")

    # Get sessions associated with the user
    sessions = keycloak_admin.get_sessions(user_id="user-id-keycloak")

    # Get themes, social providers, auth providers, and event listeners available on this server
    server_info = keycloak_admin.get_server_info()

    # Get clients belonging to the realm Returns a list of clients belonging to the realm
    clients = keycloak_admin.get_clients()

    # Get client - id (not client-id) from client by name
    client_id = keycloak_admin.get_client_id("my-client")

    # Get representation of the client - id of client (not client-id)
    client = keycloak_admin.get_client(client_id="client_id")

    # Get all roles for the realm or client
    realm_roles = keycloak_admin.get_realm_roles()

    # Get all roles for the client
    client_roles = keycloak_admin.get_client_roles(client_id="client_id")

    # Get client role
    role = keycloak_admin.get_client_role(client_id="client_id",
                                          role_name="role_name")

    # Warning: Deprecated
    # Get client role id from name
    role_id = keycloak_admin.get_client_role_id(client_id="client_id",
                                                role_name="test")

    # Create client role
    keycloak_admin.create_client_role(client_role_id='client_id',
                                      payload={'name': 'roleName',
                                               'clientRole': True})

    # Assign client role to user. Note that BOTH role_name and role_id appear to be required.
    keycloak_admin.assign_client_role(client_id="client_id", user_id="user_id",
                                      role_id="role_id", role_name="test")

    # Retrieve client roles of a user.
    keycloak_admin.get_client_roles_of_user(user_id="user_id",
                                            client_id="client_id")

    # Retrieve available client roles of a user.
    keycloak_admin.get_available_client_roles_of_user(user_id="user_id",
                                                      client_id="client_id")

    # Retrieve composite client roles of a user.
    keycloak_admin.get_composite_client_roles_of_user(user_id="user_id",
                                                      client_id="client_id")

    # Delete client roles of a user.
    keycloak_admin.delete_client_roles_of_user(client_id="client_id",
                                               user_id="user_id",
                                               roles={"id": "role-id"})
    keycloak_admin.delete_client_roles_of_user(client_id="client_id",
                                               user_id="user_id",
                                               roles=[{"id": "role-id_1"},
                                                      {"id": "role-id_2"}])

    # Get all client authorization resources
    client_resources = get_client_authz_resources(client_id="client_id")

    # Get all client authorization scopes
    client_scopes = get_client_authz_scopes(client_id="client_id")

    # Get all client authorization permissions
    client_permissions = get_client_authz_permissions(client_id="client_id")

    # Get all client authorization policies
    client_policies = get_client_authz_policies(client_id="client_id")

    # Create new group
    group = keycloak_admin.create_group({"name": "Example Group"})

    # Get all groups
    groups = keycloak_admin.get_groups()

    # Get group
    group = keycloak_admin.get_group(group_id='group_id')

    # Get group by name
    group = keycloak_admin.get_group_by_path(path='/group/subgroup',
                                             search_in_subgroups=True)

    # Function to trigger user sync from provider
    sync_users(storage_id="storage_di", action="action")

    # Get client role id from name
    role_id = keycloak_admin.get_client_role_id(client_id=client_id,
                                                role_name="test")

    # Get all roles for the realm or client
    realm_roles = keycloak_admin.get_roles()

    # Assign client role to user. Note that BOTH role_name and role_id appear to be required.
    keycloak_admin.assign_client_role(client_id=client_id, user_id=user_id,
                                      role_id=role_id, role_name="test")

    # Assign realm roles to user
    keycloak_admin.assign_realm_roles(user_id=user_id, roles=realm_roles)

    # Get all ID Providers
    idps = keycloak_admin.get_idps()

    # Create a new Realm
    keycloak_admin.create_realm(payload={"realm": "demo"}, skip_exists=False)