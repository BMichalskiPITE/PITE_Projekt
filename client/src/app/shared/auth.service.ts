import { 
    Injectable,
    OnInit,
} from '@angular/core';
import { LoggedUser } from '../commons/loggedUser';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';
import { GlobalState } from './global.state';
import { Observable } from 'rxjs/Observable';
import { RestService } from './rest.service';
@Injectable()
export class AuthService {

    private loggedUser:BehaviorSubject<LoggedUser> = new BehaviorSubject<LoggedUser>(undefined);
    constructor(private rest: RestService) { }

    isLogged():boolean {
        return !!this.loggedUser.getValue();
    }

    getLoggedUser():LoggedUser {
        return this.loggedUser.getValue();
    }

    subscribeLoggedUser():Observable<LoggedUser> {
        return this.loggedUser;
    }

    setLoggedUser(user:LoggedUser):void {
        user.is_guide = true;
        this.rest.tryRegister(user).then( r=> {
            this.rest.getUser(user.id).then(r2 => {
                const userek = r2;
                userek.roles = ["tourist"]
                if(userek.is_guide){
                    userek.roles.push("guide")
                }
                this.loggedUser.next(userek);
            })
        }).catch(e => 
            this.rest.getUser(user.id).then(r2 => {
                const userek = r2;
                userek.roles = ["tourist"]
                if(userek.is_guide){
                    userek.roles.push("guide")
                }
                this.loggedUser.next(userek);
            })
            .catch(e=>e)
        );
    }

    isGuideNow(): boolean {
        const logged:LoggedUser = this.getLoggedUser();
        return logged && logged.is_guide;
    }

    logout():void {
        this.loggedUser.next(undefined);
    }
}
