import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Place } from './place';
import { environment } from '../environments/environment';
import { RestService } from './shared/rest.service';

@Injectable()
export class PlacesService {
  constructor(private rest: RestService) { }

  getPlaces() {
    return this.rest.getAllPlaces();
  }
}