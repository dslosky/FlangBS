import { ModuleWithProviders } from '@angular/core';
import { Routes, RouterModule }   from '@angular/router';

// all routes
const appRoutes: Routes = [
];

// admin and login guards
export const appRoutingProviders: any[] = [
];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);
