import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app.routing';
import { AppComponent } from './app.component';
import { CaDataService } from './services/ca-data.service';
import { PostsComponent } from './components/posts/posts.component';
import { NotificationsComponent } from './components/notifications/notifications.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { GuidelinesComponent } from './components/guidelines/guidelines.component';
import { LeaderboardComponent } from './components/leaderboard/leaderboard.component';
import { CaProfileComponent } from './components/ca-profile/ca-profile.component';
import { TasksComponent } from './components/tasks/tasks.component';
import { EventsComponent } from './components/events/events.component';
  
@NgModule({
  declarations: [
    AppComponent,
    PostsComponent,
    PostsComponent,
    NotificationsComponent,
    SidebarComponent,
    NavbarComponent,
    GuidelinesComponent,
    LeaderboardComponent,
    CaProfileComponent,
    TasksComponent,
    EventsComponent,
  ],
  imports: [
    BrowserModule,
    HttpModule,
    FormsModule,
    AppRoutingModule,
  ],
  providers: [
  	CaDataService,
  	],
  bootstrap: [AppComponent, NavbarComponent, SidebarComponent]
})
export class AppModule { }

//https://stackoverflow.com/questions/34672987/django-with-angular-2/39438567#39438567