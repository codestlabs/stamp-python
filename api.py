from .lib.ai.oaiftrs.oaiftrs import NLPText, SmartSearch, OptimizationAI
from .lib.ai.oaiftrs.ptr.ptai import PatternAI
from .lib.ai.oaiftrs.cdi.coai import CodeAI
from .lib.ai.oaiftrs.daz.daai import DataAnalyzer
from .lib.ai.oaiftrs.prd.prai import PredictSystem
from .lib.ai.oaiftrs.sec.scai import SecurityAI
from .lib.ai.oaiftrs.img.imai import ImageAI
from .lib.ai.oaiftrs.aud.adai import AudioAI
from .lib.ai.oaiftrs.dpl.dlai import DeepLearningAI
from .lib.ai.oaiftrs.fct.fcai import ForecastAI
from .lib.ai.oaiftrs.kga.kgai import KnowledgeGraphAI
from .lib.ai.oaiftrs.rec.rcai import RecommendationAI
from .lib.ai.oaiftrs.vis.viai import VisionAI
from .lib.ai.oaiftrs.qzr.quzr import QuantizerAI
import inspect
class AI:
	NLPText = NLPText
	SmartSearch = SmartSearch
	OptimizationAI = OptimizationAI
	PatternAI = PatternAI
	CodeAI = CodeAI
	DataAnalyzer = DataAnalyzer
	PredictSystem = PredictSystem
	SecurityAI = SecurityAI
	ImageAI = ImageAI
	AudioAI = AudioAI
	DeepLearningAI = DeepLearningAI
	ForecastAI = ForecastAI
	KnowledgeGraphAI = KnowledgeGraphAI
	RecommendationAI = RecommendationAI
	VisionAI = VisionAI
	QuantizerAI = QuantizerAI
class DevTools:
    @staticmethod
    def caller(depth=1):
        s = inspect.stack()
        return s[depth].filename if len(s) > depth else None
    @staticmethod
    def assert_true(expr, msg="Assertion failed"):
        if not expr:
            raise AssertionError(msg)
        return True