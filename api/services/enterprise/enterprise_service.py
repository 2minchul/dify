from services.enterprise.base import EnterpriseRequest


class EnterpriseService:

    @classmethod
    def get_info(cls) -> dict:
        # return EnterpriseRequest.send_request('GET', '/info')

        # class SystemFeatureModel(BaseModel):
        #     sso_enforced_for_signin: bool = False
        #     sso_enforced_for_signin_protocol: str = ''
        #     sso_enforced_for_web: bool = False
        #     sso_enforced_for_web_protocol: str = ''
        return {
            'sso_enforced_for_signin': False,
            'sso_enforced_for_signin_protocol': '',
            'sso_enforced_for_web': False,
            'sso_enforced_for_web_protocol': '',
        }
