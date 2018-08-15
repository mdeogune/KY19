import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';

import { CaDataService } from './services/ca-data.service';
import { PostsComponent } from './components/posts/posts.component';
// import { NotificationsComponent } from './components/notifications/notifications.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { NavbarComponent } from './components/navbar/navbar.component';
// import { GuidelinesComponent } from './components/guidelines/guidelines.component';
import { CaProfileComponent } from './components/ca-profile/ca-profile.component';
// import { LeaderboardComponent } from './components/leaderboard/leaderboard.component';
// import { TasksComponent } from './components/tasks/tasks.component';
import { EventsComponent } from './components/events/events.component';

const  BASE_URL : string = 'dashboard';
const appRoutes: Routes = [
	{
		path: BASE_URL,
		component: PostsComponent,
	},
    {
        path: BASE_URL + '/user-profile',
        component: CaProfileComponent,
    },
    {
        path: BASE_URL + '/events',
        component: EventsComponent,
    }
]

@NgModule({
    imports: [
        RouterModule.forRoot(
            appRoutes
        )
    ],
    exports: [
        RouterModule
    ]
})
export class AppRoutingModule{}

//https://angular.io/guide/forms