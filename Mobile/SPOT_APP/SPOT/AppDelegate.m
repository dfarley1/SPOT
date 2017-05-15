// Copyright 2015 Google Inc. All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#import "AppDelegate.h"
#import <UserNotifications/UserNotifications.h>
// define macro
#define SYSTEM_VERSION_GRATERTHAN_OR_EQUALTO(v)  ([[[UIDevice currentDevice] systemVersion] compare:v options:NSNumericSearch] != NSOrderedAscending)
@interface AppDelegate ()

@end

@implementation AppDelegate

static NSString *kServerSessionCookie = @"PHPSESSID";
static NSString *kLocalCookieName = @"MyProjectCookie";
static NSString *kLocalUserData = @"MyProjectLocalUser";
static NSString *kBaseUrl = @"https://alien-walker-157903.appspot.com/api/v1/auth/login/";

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    // Override point for customization after application launch.
    [self updateSession];
    
    if ([self isLoggedIn]) {
        // action if currently logged in
    } else {
        // action if currently not logged in
    }
    
    [self registerForRemoteNotification];
    
    return YES;
}

- (void)applicationWillResignActive:(UIApplication *)application {
    // Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
    // Use this method to pause ongoing tasks, disable timers, and invalidate graphics rendering callbacks. Games should use this method to pause the game.
}

- (void)saveLoginSession
{
    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
    
    NSArray *allCookies = [[NSHTTPCookieStorage sharedHTTPCookieStorage] cookiesForURL:[NSURL URLWithString:kBaseUrl]];
    for (NSHTTPCookie *cookie in allCookies) {
        if ([cookie.name isEqualToString:kServerSessionCookie]) {
            NSMutableDictionary* cookieDictionary = [NSMutableDictionary dictionaryWithDictionary:[defaults dictionaryForKey:kLocalCookieName]];
            [cookieDictionary setValue:cookie.properties forKey:kBaseUrl];
            [defaults setObject:cookieDictionary forKey:kLocalCookieName];
            [defaults synchronize];
            
            break;
        }
    }
}

// 4.
- (void)removeLoginSession
{
    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
    [defaults removeObjectForKey:kLocalCookieName];
    [defaults synchronize];
}
// 5.
- (void)updateSession
{
    NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
    NSDictionary *cookieDict = [defaults dictionaryForKey:kLocalCookieName];
    NSDictionary *cookieProperties = [cookieDict valueForKey:kBaseUrl];
    if (cookieProperties != nil) {
        NSHTTPCookie *cookie = [NSHTTPCookie cookieWithProperties:cookieProperties];
        NSArray *cookies = [NSArray arrayWithObject:cookie];
        [[NSHTTPCookieStorage sharedHTTPCookieStorage] setCookies:cookies forURL:[NSURL URLWithString:kBaseUrl] mainDocumentURL:nil];
    }
}
- (BOOL)isLoggedIn
{
    return [[NSUserDefaults standardUserDefaults] objectForKey:kLocalCookieName] != nil;
}

- (void)applicationDidEnterBackground:(UIApplication *)application {
    // Use this method to release shared resources, save user data, invalidate timers, and store enough application state information to restore your application to its current state in case it is terminated later.
    // If your application supports background execution, this method is called instead of applicationWillTerminate: when the user quits.
}


- (void)applicationWillEnterForeground:(UIApplication *)application {
    // Called as part of the transition from the background to the active state; here you can undo many of the changes made on entering the background.
}


- (void)applicationDidBecomeActive:(UIApplication *)application {
    // Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
}


- (void)applicationWillTerminate:(UIApplication *)application {
    // Called when the application is about to terminate. Save data if appropriate. See also applicationDidEnterBackground:.
}

//#pragma mark - Remote Notification Delegate // <= iOS 9.x
//
//- (void)application:(UIApplication *)application didRegisterUserNotificationSettings:(UIUserNotificationSettings *)notificationSettings {
//    [application registerForRemoteNotifications];
//}
//
//- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken{
//    NSString *strDevicetoken = [[NSString alloc]initWithFormat:@"%@",[[deviceToken.description stringByTrimmingCharactersInSet:[NSCharacterSet characterSetWithCharactersInString:@"<>"]] stringByReplacingOccurrencesOfString:@" " withString:@""]];
//    NSLog(@"Device Token = %@",strDevicetoken);
//    self.strDeviceToken = strDevicetoken;
//}
//
//-(void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo
//{
//    NSLog(@"Push Notification Information : %@",userInfo);
//}
//
//-(void)application:(UIApplication *)application didFailToRegisterForRemoteNotificationsWithError:(NSError *)error
//{
//    NSLog(@"%@ = %@", NSStringFromSelector(_cmd), error);
//    NSLog(@"Error = %@",error);
//}

#pragma mark - UNUserNotificationCenter Delegate // >= iOS 10

- (void)userNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler{
    
    NSLog(@"User Info = %@",notification.request.content.userInfo);
    
    completionHandler(UNNotificationPresentationOptionAlert | UNNotificationPresentationOptionBadge | UNNotificationPresentationOptionSound);
}

- (void)userNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void(^)())completionHandler{
    
    NSLog(@"User Info = %@",response.notification.request.content.userInfo);
    completionHandler();
}

#pragma mark - Class Methods

/**
 Notification Registration
 */
- (void)registerForRemoteNotification {
    if(SYSTEM_VERSION_GRATERTHAN_OR_EQUALTO(@"10.0")) {
        UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
        center.delegate = self;
        [center requestAuthorizationWithOptions:(UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge) completionHandler:^(BOOL granted, NSError * _Nullable error){
            if( !error ){
                [[UIApplication sharedApplication] registerForRemoteNotifications];
            }
        }];
    }
//    else {
//        [[UIApplication sharedApplication] registerUserNotificationSettings:[UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeSound | UIUserNotificationTypeAlert | UIUserNotificationTypeBadge) categories:nil]];
//        [[UIApplication sharedApplication] registerForRemoteNotifications];
//    }
}
@end
