import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';

import { PagesComponent } from './pages.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { UserProfileComponent } from './user/userProfile.component';
import { GuideComponent } from "./guide/guide.component";
import { TouristComponent } from "./tourist/tourist.component";
import { TouristAuthGuard, GuideAuthGuard} from '../shared/authGuard';
import { ModuleWithProviders } from '@angular/compiler/src/core';
import { AddTripComponent } from './tourist/addTrip/addTrip.component';
import { AllTripsComponent } from './tourist/allTrips/allTrips.component';
import { TripDetailsComponent } from './tourist/tripDetails/tripDetails.component';

const routes: Routes = [{
  path: '',
  component: PagesComponent,
  children: [
    {
      path: 'dashboard',
      component: DashboardComponent,
    },
    {
      path: '',
      redirectTo: 'dashboard',
      pathMatch: 'full',
    },
    {
      path:'profile',
      component: UserProfileComponent,
      // canActivate: [TouristAuthGuard]
    },
    {
      path:'tourist',
      //component: TouristComponent,
      //canActivate: [TouristAuthGuard]
      children:[
        {
          path:'trip',
          component: AddTripComponent,
        },
        {
          path:'trips',
          component: AllTripsComponent
        },
        {
          path: 'tripDetails/:id',
          component: TripDetailsComponent
        }
      ]
    },
    {
      path:'guide',
      children:[
        {
          path:'find',
          component: AddTripComponent,
        },
        {
          path:'trips',
          component: AllTripsComponent
        }
      ]
    }
  ],
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
  providers: [
  ]
})
export class PagesRoutingModule {
}
