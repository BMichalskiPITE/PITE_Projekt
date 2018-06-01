import { NgModule } from '@angular/core';
import { GlobalState } from './global.state';
import { ModuleWithProviders } from '@angular/core/src/metadata/ng_module';
import { AuthService } from './auth.service';
import { RestService } from './rest.service';
import { TouristAuthGuard, GuideAuthGuard } from './authGuard';

@NgModule({})
export class SharedModule {
    static forRoot():ModuleWithProviders {
        return {
            ngModule: SharedModule,
            providers: [
                GlobalState,
                AuthService,
                RestService,
                TouristAuthGuard,
                // GuideAuthGuard,
            ]
        }
    }
}
