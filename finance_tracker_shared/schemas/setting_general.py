from pydantic import BaseModel, field_validator, model_validator
import pycountry

KEYS = ["country_code", "default_currency", "default_currency_symbol"]

CURRENCY_SYMBOLS = [
    "د.إ", "؋", "L", "֏", "ƒ", "Kz", "$", "₼", "KM", "৳", "лв", ".د.ب", "FBu",
    "$b", "R$", "฿", "Nu.", "P", "Br", "BZ$", "FC", "CHF", "¥", "₡", "₱", "Kč",
    "Fdj", "kr", "RD$", "دج", "£", "Nfk", "Ξ", "€", "₾", "₵", "GH₵", "D", "FG",
    "Q", "L", "kn", "G", "Ft", "Rp", "₪", "₹", "ع.د", "﷼", "J$", "JD", "KSh",
    "лв", "៛", "CF", "₩", "KD", "₸", "₭", "₨", "M", "Ł", "Lt", "Ls", "LD", "lei",
    "Ar", "ден", "K", "₮", "MOP$", "UM", "Rf", "MK", "RM", "MT", "₦", "C$", "B/.",
    "S/.", "zł", "Gs", "￥", "Дин.", "₽", "R₣", "ج.س.", "Le", "S", "Db", "E", "SM",
    "T", "د.ت", "T$", "₤", "₺", "TT$", "NT$", "TSh", "₴", "USh", "$U", "VT",
    "WS$", "FCFA", "Ƀ", "CFA", "₣", "R", "Z$"]

class SettingGeneralBase(BaseModel):
    key: str
    value: str

    @property
    def norm_key(self) -> str:
        return self.key.replace("_", " ").capitalize()

    @field_validator("key")
    def validate_key(cls, key: str) -> str:
        if not key or key not in KEYS:
            raise ValueError(f"Key must be one of {KEYS}")
        return key

    @field_validator("value")
    def validate_value(cls, value: str) -> str:
        if not value or len(value) > 20:
            raise ValueError("Value cannot be empty and must not exceed 20 characters")
        return value

    @model_validator(mode="after")
    def validate_combination(self) -> "SettingGeneralBase":
        key = self.key
        value = self.value

        if key == "country_code":
            if not pycountry.countries.get(alpha_2=value.upper()):
                raise ValueError(f"Invalid country code: {value}")
            else:
                value = value.upper()
        
        elif key == "default_currency":
            if not pycountry.currencies.get(alpha_3=value.upper()):
                raise ValueError(f"Invalid currency code: {value}")
            self.value = value.upper()

        elif key == "default_currency_symbol":
            if value not in CURRENCY_SYMBOLS:
                raise ValueError(f"Invalid currency symbol: {value}")

        return self

class SettingGeneralCreate(SettingGeneralBase):
    pass

class SettingGeneralRead(SettingGeneralBase):
    id: int

    model_config = {
        "from_attributes": True
    }
