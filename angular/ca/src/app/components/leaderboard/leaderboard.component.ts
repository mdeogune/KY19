import { Component, OnInit } from '@angular/core';
import { CaDataService } from '../../services/ca-data.service';

@Component({
  selector: 'app-leaderboard',
  templateUrl: './leaderboard.component.html',
  styleUrls: ['./leaderboard.component.css']
})
export class LeaderboardComponent implements OnInit {
  public ca_total_points: number;
  constructor(public caservice: CaDataService) { }
  public userData: JSON;
  ngOnInit(): void {
  	this.caservice.getLeaderBoard()
  	.then((data)=>{
  		console.log(data);
  		this.userData = data.json()['top_points'];
      this.ca_total_points = data.json()['ca_points']['total_points']; 
  	})
  }

}
