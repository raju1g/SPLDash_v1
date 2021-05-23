from typing import NamedTuple, List, Dict
import enum


# Constants
class BackgroundColor(enum.Enum):
    GREEN = "green-bg"
    DARK_GREEN = "dark-green-bg"
    GREY = "grey-bg"
    LIGHT_BLUE = "lightblue-bg"
    GREY_GRADIENT = "grey-gradient-bg"
    LIGHT_BLUE_GRADIENT = "light-blue-gradient-bg"
    DARK_BLUE = "darkblue-bg"
    SIMULATOR_CARD_BG = "simulator-card-bg"


class FontColor(enum.Enum):
    GREY = "grey-span"
    LIGHT_BLUE = "lightblue-span"
    DARK_BLUE = "darkblue-span"


class Document(enum.Enum):
    METHODOLOGY = "https://docs.google.com/document/d/1C7LyLmeeQVV0A3vRqH03Ru0ABdJ6hCOcv_lYVMPQy2M/edit"
    FAQ = "https://docs.google.com/document/d/1lanC52PjzU2taQISs1kO9mEJPtvwZM4uyvnHL9IalbQ/edit"
    GITHUB = "https://github.com/ImpulsoGov/simulacovid/tree/master/COVID19_App"


class Logo(enum.Enum):
    IMPULSO = "https://i.imgur.com/zp9QCDU.png"
    CORONACIDADES = "https://i.imgur.com/BamxSJE.png"
    ARAPYAU = "https://i.imgur.com/SjsMK2A.jpg"
    SESI = "https://imgur.com/Crnlwf8.jpg"


class Link(enum.Enum):
    AMBASSADOR_FORM = "https://forms.gle/iPFE7T6Wrq4JzoEw9"
    YOUTUBE_TUTORIAL = "https://www.youtube.com/watch?v=-4Y0wHMmWAs"


class Illustration(enum.Enum):
    CITY = "https://i.imgur.com/UP2ZylF.png"
    BUILDING = "https://i.imgur.com/zaGvVzy.png"


class IndicatorType(enum.Enum):
    PRO1 = "p1"
    PRO2 = "p2"
    PRO3 = "p3"
    PRO4 = "p4"
    PRO5 = "p5"


class AlertBackground(enum.Enum):
    hide = ""
    green = "voitto"
    yellow = "tasapeli"
    orange = "havio"
    red = "havi"


class IndicatorBackground(enum.Enum):
    hide = "nan"
    green = 0
    yellow = 1
    orange = 2
    red = 3


# Models
class Indicator:
    def __init__(
        self,
        header,
        caption,
        unit,
        left_label,
        right_label,
        last_updated=None,
        risk="nan",
        display="",
        left_display="",
        right_display="",
    ):
        self.header = header
        self.caption = caption
        self.unit = unit
        self.display = display
        self.risk = risk
        self.left_label = left_label
        self.right_label = right_label
        self.left_display = left_display
        self.right_display = right_display
        self.last_updated = last_updated


IndicatorCards: Dict[str, Indicator] = {
    IndicatorType.PRO1.value: Indicator(
        header="Projekti 1",
        caption="Parannamme Palloliiton perusjärjestelmien ja verkkopalvelujen käytettävyyttä",
        unit="%",
        left_label="Current tasks:",
        right_label="State of current task:",
    ),
    IndicatorType.PRO2.value: Indicator(
        header="Projekti 2",
        caption="Paranname Palloliiton perusjärjestelmien ja verkkopalvelujen käytettävyyttä",
        unit="%",
        left_label="Current tasks:",
        right_label="State of current task:",
    ),
    IndicatorType.PRO3.value: Indicator(
        header="Projekti 3",
        caption="Parannamme Palloliiton perusjärjestelmien ja verkkopalvelujen käytettävyyttä",
        unit="%",
        left_label="Current tasks:",
        right_label="State of current task:",
    ),
    # TODO -> VOLTAR PROJECAO DE LEITOS
    # caption="Se nada mudar, todos os leitos de seu <b>estado ou regional de saúde</b> estarão ocupados em",
    # unit="dia(s)",
    IndicatorType.PRO4.value: Indicator(
        header="Projekti 4",
        caption="Parannamme Palloliiton perusjärjestelmien ja verkkopalvelujen käytettävyyttä",
        unit="%",
        left_label="Current tasks:",
        right_label="State of current task:",
    ),
    IndicatorType.PRO5.value: Indicator(
        header="Projekti 5",
        caption="Parannamme Palloliiton perusjärjestelmien ja verkkopalvelujen käytettävyyttä",
        unit="%",
        left_label="Current tasks:",
        right_label="State of current task:",
    ),
}


class Product:
    def __init__(self, name, caption: str, image: Illustration, recommendation=""):
        self.recommendation = recommendation
        self.name = name
        self.caption = caption
        self.image = image


ProductCards: List[Product] = [
    Product(
        recommendation="Explore",
        name="Saúde em Ordem<br>",
        caption="Quais atividades econômicas meu município deveria reabrir primeiro?",
        image="https://i.imgur.com/M0jr43n.png",
    ),
    Product(
        recommendation="Navegue",
        name="Onda Covid<br>",
        caption="Onde meu estado está na curva da doença?",
        image="https://i.imgur.com/Oy7IiGB.png",
    ),
]


class Dimension:
    def __init__(self, text):
        self.text = text


DimensionCards: List[Dimension] = [
    Dimension(
        text="<b>1. Situação da doença,</b> que busca medir como a doença está se espalhando no território.",
    ),
    Dimension(
        text="<b>2. Controle da doença,</b> que retrata a capacidade do poder público de detectar os casos.",
    ),
    Dimension(
        text="<b>3. Capacidade de respostas do sistema de saúde,</b> que reflete a situação do sistema de saúde e risco de colapso.",
    ),
    Dimension(
        text="<b>4. Confiança dos dados,</b> que reflete a qualidade das medições de casos sendo feitas pelos governos.",
    ),
]
