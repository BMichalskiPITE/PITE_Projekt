import { Component, OnInit, OnDestroy } from '@angular/core';
import { Place } from '../../../place';
import { ActivatedRoute } from '@angular/router';
import { RestService } from '../../../shared/rest.service';

@Component({
  selector: 'trip-details',
  templateUrl: './tripDetails.component.html',
  styleUrls: ['./tripDetails.component.scss']
})
export class TripDetailsComponent implements OnInit, OnDestroy {

    // details = {
    //   tripId: 12,
    //   tripName: "nazwa tripa",
    //   tripDescription: "opis ktory ktos dal",
    //   places:[
    //       {
    //           placeid: "id",
    //           latitude: 52,
    //           longitude: 21,
    //           name: "nazwa",
    //           photoRef: "CmRaAAAAEnf6pOTUJdMv0aC-5ukwXNY74FKVl-kPCEmnhX-eSodHY3ZKukK5170GUfwlrHnGj3IDhNoeqWeFe0hlDVxQBQ-iCO9fZS21234nqbqL_mRTsEGQYOnfuHB9_I6OAQstEhAJ_7GwApaE-C8hl0P5uKA9GhSFhDgeTNVC837G9LLT26SzyJWbrg"              ,
    //           vicinty: "dfghjo"
    //       }
    //     ],
    //   guides:[
    //       //lista opcjonalnych przewodnikow ktorzy chca wziac wycieczke :D
    //       {
    //         id:"id googlowe",
    //         username:"nazwa user",
    //         grade: 4.12,// jesl iwogole kiedys to zrobiimy XD
    //         selected: true
    //     },
    //     {
    //       id:"id googlowe",
    //       username:"nazwa user",
    //       grade: 4.12,// jesl iwogole kiedys to zrobiimy XD
    //       selected: false
    //     }
    //   ]
    // }
    details;
    private sub;
    id:Number;
    constructor(private activate:ActivatedRoute,
    private rest: RestService){}

    ngOnInit() {
      this.sub = this.activate.params.subscribe(params => {
         this.id = +params['id'];
         this.details = undefined;
         this.rest.getTripDetails(this.id)
         .then(t => {
            this.details = {
              tripId:t.pk,
              tripName: t.tripName,
              tripDescription: t.tripDescription,
              places: [],
              guides: []
          }
          console.log(this.details)
             for(let tr of t.places){
                 this.rest.getPlaceById(tr)
                 .then(pl => this.details.places.push(pl))
                 .catch( e => {
                     console.log(e);
                     return e;
                 })
             }
            for(let tr of t.guides){
              this.rest.getUser(tr)
              .then(pl => this.details.guides.push(pl))
              .catch( e => {
                  console.log(e);
                  return e;
              })
          }
         })
         .catch(e => {
             console.log(e)
             this.details = undefined;
         })
      });

    }
  
    ngOnDestroy() {
      this.sub.unsubscribe();
    }
}
