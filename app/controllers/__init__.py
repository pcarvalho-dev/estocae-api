from app.controllers.base_crud import CRUDBase

from .. import models
from .. import schemas

# Creating a new instance of CRUDBase class.
crud_city = CRUDBase(models.City, schemas.CitySchema)
crud_country = CRUDBase(models.Country, schemas.CountrySchema)
crud_group = CRUDBase(models.Group, schemas.GroupSchema)
crud_state = CRUDBase(models.State, schemas.StateSchema)
crud_user_address = CRUDBase(models.UserAddress, schemas.UserAddressSchema)
crud_community = CRUDBase(models.Community, schemas.CommunitySchema)
crud_main_company_address = CRUDBase(models.MainCompanyAddress,
                                     schemas.MainCompanyAddressSchema)
crud_main_settings = CRUDBase(models.MainSettings,
                              schemas.MainSettingsSchema)
crud_user_code_password = CRUDBase(models.UserCodePassword,
                                   schemas.UserCodePassword,
                                   schemas.UserCodePassword,
                                   schemas.UserCodePassword)
crud_plan = CRUDBase(models.Plan, schemas.PlanSchema)
crud_offer = CRUDBase(models.Offer, schemas.OfferSchema)
crud_coupon = CRUDBase(models.Coupon, schemas.CouponSchema)
crud_product_page = CRUDBase(models.ProductPage, schemas.ProductPageSchema)
crud_product_checkout = CRUDBase(models.ProductCheckout, schemas.ProductCheckoutSchema)
crud_product_affiliate = CRUDBase(models.ProductAffiliate, schemas.ProductAffiliateSchema)
