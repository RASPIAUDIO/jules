
#include "esphome.h"

namespace esphome {
namespace globals_save {

class GlobalsSaveAction : public Action<> {
public:
    GlobalsSaveAction(GlobalsComponent *globals) : globals_{globals} {}

    void play() override {
        globals_->save();
    }

protected:
    GlobalsComponent *globals_;
};

} // namespace globals_save
} // namespace esphome
