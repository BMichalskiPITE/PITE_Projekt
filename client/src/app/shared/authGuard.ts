import {
    CanActivate,
    ActivatedRouteSnapshot,
    RouterStateSnapshot
} from "@angular/router";
import { AuthService } from './auth.service';
import { Injectable } from "@angular/core";
import { Router } from "@angular/router";

@Injectable()
export class GuideAuthGuard implements CanActivate {

    constructor(private auth: AuthService, private router: Router) {}

    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot):boolean {
        if(this.auth.isGuideNow()){
            return true;
        }else {
            this.router.navigate(['/']);
            return false;
        }
    }
}

@Injectable()
export class TouristAuthGuard implements CanActivate{

    constructor(private auth: AuthService, private router: Router) {}

    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot):boolean {
        if( this.auth.isLogged()){
            return true;
        }else {
            this.router.navigate(['/']);
            return false;
        }
    }
}

// export class UniqueAuthGuard implements CanActivate {
    
//     constructor(private auth: AuthService) {}

//     canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot):boolean {
//         const isLogged = !!this.auth.getLoggedUser();
//         const roles = isLogged ? this.auth.getLoggedUser().roles : [];
//         //todo find from menu in pagesComponent current view by url path,
//         //and depends on permission grand access
//         return true;
//     }

// }