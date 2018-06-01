import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { NbMenuService, NbSidebarService } from '@nebular/theme';
import { UserService } from '../../../user.service';
import { AnalyticsService } from '../../../@core/utils/analytics.service';
import { LoggedUser } from '../../../commons/loggedUser';
import { GlobalState } from '../../../shared/global.state';
import {
  AuthService as SocialAuthService,
  GoogleLoginProvider,
} from 'angular5-social-login';
import { AuthService } from '../../../shared/auth.service';
import { OnDestroy } from '@angular/core/src/metadata/lifecycle_hooks';
import { Subscription } from 'rxjs/Subscription';


@Component({
  selector: 'ngx-header',
  styleUrls: ['./header.component.scss'],
  templateUrl: './header.component.html',
})
export class HeaderComponent implements OnInit, OnDestroy {


  @Input() position = 'normal';
  user: LoggedUser;
  subscription:Subscription;
  userMenu = [{ title: 'Profile' }, { title: 'Log out', link: 'logout' }];

  constructor(private sidebarService: NbSidebarService,
              private menuService: NbMenuService,
              private authService: AuthService,
              private analyticsService: AnalyticsService,
              private socialAuthService: SocialAuthService,
              private router: Router) {
  }

  ngOnInit() {
    this.subscription = this.authService.subscribeLoggedUser().subscribe( user => {
      this.user = user;
    });
    
    
  }

  ngOnDestroy():void {
    this.subscription.unsubscribe();
  }

  toggleSidebar(): boolean {
    this.sidebarService.toggle(true, 'menu-sidebar');
    return false;
  }

  toggleSettings(): boolean {
    this.sidebarService.toggle(false, 'settings-sidebar');
    return false;
  }

  goToHome() {
    this.menuService.navigateHome();
  }

  startSearch() {
    this.analyticsService.trackEvent('startSearch');
  }

  public socialSignIn() {
    let socialPlatformProvider = GoogleLoginProvider.PROVIDER_ID;
    
    this.socialAuthService.signIn(socialPlatformProvider).then(
      (userData) => {
        
        const loggedUser = new LoggedUser(
          userData.id,
          userData.idToken,
          userData.name,
          userData.email,
          userData.image
        );
        this.authService.setLoggedUser(loggedUser);
      });
  }

  logout() {
    this.socialAuthService.signOut().then(
      data => {
          this.router.navigate(["/"]);
          this.authService.logout();
      }
    ).catch(e => e);
  }

  viewProfile():void {
    this.router.navigate(['/profile',this.user.id]);
  }
}
