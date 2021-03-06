from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class FoursquareAccount(ProviderAccount):
    def get_profile_url(self):
        return 'https://foursquare.com/user/' + self.account.extra_data.get('response').get('user').get('id')

    def get_avatar_url(self):
        return self.account.extra_data.get('response').get('user').get('photo')

    #def to_str(self):
    #    dflt = super(FoursquareAccount, self).to_str()
    #    return self.account.extra_data.get('name', dflt)


class FoursquareProvider(OAuth2Provider):
    id = 'foursquare'
    name = 'Foursquare'
    package = 'allauth.socialaccount.providers.foursquare'
    account_class = FoursquareAccount

    def extract_uid(self, data):
        return str(data['response']['user']['id'])

    def extract_common_fields(self, data):
        return dict(firstname=data.get('response').get('user').get('firstname'),
                    lastname=data.get('response').get('user').get('lastname'),
                    email=data.get('response').get('user').get('contact').get('email'))


providers.registry.register(FoursquareProvider)