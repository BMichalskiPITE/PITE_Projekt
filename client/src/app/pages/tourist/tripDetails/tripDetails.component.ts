import { Component, OnInit, OnDestroy } from '@angular/core';
import { Place } from '../../../place';
import { ActivatedRoute } from '@angular/router';
import {NgbModal, ModalDismissReasons} from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'trip-details',
  templateUrl: './tripDetails.component.html',
  styleUrls: ['./tripDetails.component.scss']
})
export class TripDetailsComponent implements OnInit, OnDestroy {

  closeResult: string;
    details = {
      tripId: 12,
      tripName: "nazwa tripa",
      tripDescription: "opis ktory ktos dal",
      places:[
          {
              placeid: "id",
              latitude: 52,
              longitude: 21,
              name: "nazwa",
              photoRef: "CmRaAAAAEnf6pOTUJdMv0aC-5ukwXNY74FKVl-kPCEmnhX-eSodHY3ZKukK5170GUfwlrHnGj3IDhNoeqWeFe0hlDVxQBQ-iCO9fZS21234nqbqL_mRTsEGQYOnfuHB9_I6OAQstEhAJ_7GwApaE-C8hl0P5uKA9GhSFhDgeTNVC837G9LLT26SzyJWbrg"              ,
              vicinty: "dfghjo"
          }
        ],
      guides:[
          //lista opcjonalnych przewodnikow ktorzy chca wziac wycieczke :D
          {
            id:"id googlowe",
            username:"nazwa user",
            grade: 4.12,// jesl iwogole kiedys to zrobiimy XD
            selected: false
        },
        {
          id:"id googlowe2",
          username:"nazwa user2",
          grade: 4.22,// jesl iwogole kiedys to zrobiimy XD
          selected: false
        }
      ]
    }
    private sub;
    id:Number;
    constructor(private activate:ActivatedRoute, private modalService: NgbModal){}

    open(content) {
    this.modalService.open(content).result.then((result) => {
      this.closeResult = `Closed with: ${result}`;
    }, (reason) => {
      this.closeResult = `Dismissed ${this.getDismissReason(reason)}`;
    });
  }

  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return 'by pressing ESC';
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return 'by clicking on a backdrop';
    } else {
      return  `with: ${reason}`;
    }
  }


    ngOnInit() {
      this.sub = this.activate.params.subscribe(params => {
         this.id = +params['id'];
      });
    }
  
    ngOnDestroy() {
      this.sub.unsubscribe();
    }

    selectGuide(guide):void{
      //this.id = details.guides.find(guide => guide.id === id)
      //details.guides[this.id].selected = true;
      let updateGuide = this.details.guides.find(this.findIndexToUpdate, guide.id)
      let index = this.details.guides.indexOf(updateGuide);
       this.details.guides[index].selected = true;

      //this.details.guides[0].selected=true;
    }

    findIndexToUpdate(newItem) { 
        return newItem.id === this;
  }
  
}
