import { 
    Injectable,
    OnInit,
} from '@angular/core';
import { Http, Response } from '@angular/http';
import { environment } from '../../environments/environment'
import { Observable } from 'rxjs/Observable';
import { Place } from '../place';
import { Message } from '../message';

@Injectable()
export class RestService {

    constructor(private http: Http) { }

    private GET(url:string) {
        return this.http.get(url).toPromise().then((r:Response) => r.json());
    }

    private POST(url:string, body:any) {
        return this.http.post(url, body).toPromise().then((r:Response)=> r.json());
    }

    public getAllPlaces():Promise<Place[]> {
        return this.GET(environment.baseApiUrl + "api/places");
    }

    public getPlaceById(id:string): Promise<Place> {
        return this.GET(environment.baseApiUrl + "api/places/"+ id);
    }

    public addTrip(trip:any):Promise<any> {
        console.log(trip)
        return this.POST(environment.baseApiUrl + "api/trips/", trip);
    }

    public getTripDetails(tripID):Promise<any> {
        return this.GET(environment.baseApiUrl + "api/trips/"+tripID)
    }

    public getUsersTrip(userId):Promise<any> {
        return this.GET(environment.baseApiUrl + "api/trips?userid="+userId);
    }

    public getAllTrips(): Promise<any> {
        return this.GET(environment.baseApiUrl + "api/trips/");
    }

    public tryRegister(user): Promise<any> {
        return this.POST(environment.baseApiUrl+"api/users/", user);
    }
    public getUser(userID:string):Promise<any> {
        return this.GET(environment.baseApiUrl + "api/users/"+ userID);
    }
    public getUsers():Promise<any> {
        return this.GET(environment.baseApiUrl + "api/users/");
    }

    public updateUser(user):Promise<any>{
        return this.http.put(environment.baseApiUrl + "api/users/", user).toPromise();
    }

    public declareGuide(tripId:String, guideId:String):Promise<any> {
        return this.POST(environment.baseApiUrl + "api/orders/", {userId: guideId, tripId: tripId});
    }

    public removeDeclarationGuide(tripId:String, guideId:String): Promise<any> {
        return this.http.delete(environment.baseApiUrl + "api/orders?tripId="+tripId +"&userId="+guideId).toPromise();
    }

    public getUserById(id:String):Promise<any> {
        return this.GET(environment.baseApiUrl + "api/users/"+id);
    }

    public getTripsToGuide():Promise<any> {
        return this.GET(environment.baseApiUrl +"api/orders/")
    }

    public getMessages(userId: string): Promise<Message[]> {
        return this.GET(environment.baseApiUrl + "api/messages?userId=" + userId);
      }
    
    public postMessage(fromUserId: string,toUserId : string, message: string){
        return this.POST(environment.baseApiUrl + "api/messages/", {fromUserId: fromUserId, toUserId: toUserId, message: message});
    }
}
