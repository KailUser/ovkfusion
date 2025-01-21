# ⚠️ **Warning: Still in Development!** ⚠️

**OVKFusion** is a work in progress. Features are subject to change, and bugs may exist. Please be aware that some functionality might not be fully stable. Contributions and feedback are appreciated!

---

# OVKFusion

**Developer**: Syirezz Cheese | [@syirezz](https://ovk.to/syirezz)

**License**: MIT License

OVKFusion is a Python library for interacting with the ovk.to platform, offering simple and powerful functionality to access account and authentication features. This library is still in progress, so feel free to contribute and stay tuned for future updates.

## Features

- **Authentication**: Securely authenticate and retrieve tokens.
- **User Info**: Retrieve user profile information.
- **OVK Access**: Interact with OVK services using the OVK class.
- **Other Features**: More to come. [We still need complete 70% of features to be done.]

## Installation

To install the library, run:

```bash
pip install ovkfusion
```

Usage
```python
from ovkfusion import Auth, OVK, Account

# Authenticate and get token
auth = Auth("######", "########", "https://ovk.to").get_token()

# Initialize OVK and Account instances
OpenVK = OVK()
User = Account()

# Get version information
print(OpenVK.version())  # Returns: {'response': 'Altair Preview (bbcb9451-nightly)'}

# Get user profile information
print(User.getProfileInfo())  
# Returns:
# {
#     'response': {
#         'first_name': 'Syirezz',
#         'photo_200': 'https://kaslana.ovk.to/hentai/fa/fa8e3e38c371226b703d7bae313872fedba05d02c1a9e611e77c37d62c02ad3feb9d16e8221a76c7a00b0aeeb52930dab45a040dcf023a2f89e07bedfb5d0eef_cropped/normal.jpeg',
#         'nickname': 'syirezz',
#         'is_service_account': False,
#         'id': 20348,
#         'is_verified': False,
#         'verification_status': 'unverified',
#         'last_name': 'Cheese',
#         'home_town': None,
#         'status': 'Создаю OVKFusion',
#         'bdate': '16.07.2011',
#         'bdate_visibility': 1,
#         'phone': '+420 ** *** 228',
#         'relation': 0,
#         'screen_name': 'syirezz',
#         'sex': 1
#     }
# }
```

Development Status

⚠️ This library is still in progress ⚠️

This project is being actively developed. There might be bugs, incomplete features, and frequent updates. Please report any issues you encounter, and check back for updates!

Contributing

Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests. Your help is appreciated as we work to improve OVKFusion.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Thank you for using OVKFusion! We hope you find it useful and easy to integrate with ovk.to.

