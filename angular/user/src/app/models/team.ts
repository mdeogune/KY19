export class Team {

	constructor (
		public name:string,
		public parent_event: string,
		public event: string,
		public team_leader: string,
		public member: any[],
		public team_size: number,
	){}

}
