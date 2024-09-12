from abc import ABC, abstractmethod


# abc是python内置包 意思是Abstract Base Classes 用于创建抽象类

# 定义医疗物品的抽象类
class MedicalItem(ABC):
    def __init__(self, name, dosage):
        # 药物名称
        self.name = name
        # 药物用量
        self.dosage = dosage

    @abstractmethod
    def message(self):
        pass


# 定义感冒疫苗类 继承自医疗物品类
class FluVaccine(MedicalItem):
    def __init__(self, name, dosage, manufacturer):
        super().__init__(name, dosage)
        # 子类对象 制造商
        self.manufacturer = manufacturer

    def message(self):
        return f"接种 {self.name}，由 {self.manufacturer} 生产。"


# 定义感冒药物类 继承自医疗物品类
class ColdMedicine(MedicalItem):
    def __init__(self, name, dosage, active_ingredient):
        super().__init__(name, dosage)
        # 子类对象活性成分active_ingredient
        self.active_ingredient = active_ingredient

    def message(self):
        return f"服用 {self.name}，剂量为 {self.dosage}，含有 {self.active_ingredient}。"


# 使用例子
flu_vaccine = FluVaccine("流感疫苗", "1 剂", "生物制药公司")
cold_medicine = ColdMedicine("感冒药", "2 颗", "乙酰氨基酚")

print(flu_vaccine.message())
print(cold_medicine.message())
