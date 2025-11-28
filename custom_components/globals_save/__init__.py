
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.automation import ACTION_REGISTRY, Automation
from esphome.const import CONF_ID

CONFIG_SCHEMA = cv.Schema({})

globals_save_ns = cg.esphome_ns.namespace('globals_save')
GlobalsSaveAction = globals_save_ns.class_('GlobalsSaveAction', cg.Action)

@ACTION_REGISTRY.register('globals.save_to_flash', GlobalsSaveAction, cv.Schema({
    cv.Required(CONF_ID): cv.use_id(None),
}))
def globals_save_to_code(config, action_id, template_arg, args):
    paren = cg.find_cpp_variable(config[CONF_ID])
    var = cg.new_Pvariable(action_id, template_arg, paren)
    return var
