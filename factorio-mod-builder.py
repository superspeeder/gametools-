class Prototype:
  def __init__(self, data):
    self.data = data

validation = {
  "type": ("must-be-in", ("item", "recipe", "entity", "item-subgroup", "item-group", "recipe-category", "assembly-machine", "inserter")),
  "name": ("must-be-type", "string")
  "icon": ("must-be-type-custom", "path")
  "icon-size": ("must-be-type", "int")
  "ingredients": ("must-fit-format", IngredientList.gatherFormat())
}

recipe = PrototypeType(MultipleFormatDefinitions(recipe, recipe_with_mult_outputs), ExtraData(("load-order-index", Placeholder(int)), ("allow-extra-data", True)))






def validate(key, val)
