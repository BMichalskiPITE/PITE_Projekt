import { NgModule } from '@angular/core';

import { PagesComponent } from './pages.component';
import { DashboardModule } from './dashboard/dashboard.module';
import { PagesRoutingModule } from './pages-routing.module';
import { ThemeModule } from '../@theme/theme.module';
import { UserModule } from './user/user.module';
import { MapsModule } from '../commons/map/map.module';

import { TouristComponent } from './tourist/tourist.component';
import { GuideComponent } from './guide/guide.component';
import { PlacesComponent } from './places/places.component'; 
import { GlobalState } from '../shared/global.state';
import { AddTripComponent } from './tourist/addTrip/addTrip.component';
import { AllTripsComponent } from './tourist/allTrips/allTrips.component';
import { TripDetailsComponent } from './tourist/tripDetails/tripDetails.component';
import { FindTripsComponent } from './guide/findTrips/findTrips.component';
import { GuideTripsComponent } from './guide/trips/guideTrips.component';
import { MessageComponent } from './message/message.component';

const PAGES_COMPONENTS = [
  PagesComponent,
  TouristComponent,
  GuideComponent,
  PlacesComponent,
  AddTripComponent,
  AllTripsComponent,
  TripDetailsComponent,
  FindTripsComponent,
  GuideTripsComponent,
  MessageComponent
];

@NgModule({
  imports: [
    PagesRoutingModule,
    ThemeModule,
    DashboardModule,
    UserModule,
    MapsModule
  ],
  declarations: [
    ...PAGES_COMPONENTS
  ],
  providers: [
  ]
})
export class PagesModule {
}
