package com.example

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.BackHandler
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.widthIn
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Close
import androidx.compose.material3.DrawerValue
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.ModalDrawerSheet
import androidx.compose.material3.ModalNavigationDrawer
import androidx.compose.material3.NavigationDrawerItem
import androidx.compose.material3.NavigationDrawerItemDefaults
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.rememberDrawerState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.model.Screen
import com.example.ui.components.AppFooter
import com.example.ui.components.WebAddressBar
import com.example.ui.pages.HomeScreen
import com.example.ui.pages.LegalPageScreen
import com.example.ui.theme.MyApplicationTheme
import com.example.ui.tools.AgeCalculatorScreen
import com.example.ui.tools.BmiCalculatorScreen
import com.example.ui.tools.DiscountCalculatorScreen
import com.example.ui.tools.EmiCalculatorScreen
import com.example.ui.tools.PercentageCalculatorScreen
import kotlinx.coroutines.launch

class MainActivity : ComponentActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    enableEdgeToEdge()
    setContent {
      MyUsefulToolsApp()
    }
  }
}

@Composable
fun Greeting(name: String = "MY USEFUL TOOLS", modifier: Modifier = Modifier) {
  Text(text = "Hello $name!", modifier = modifier)
}

@Composable
fun MyUsefulToolsApp() {
  val systemDark = isSystemInDarkTheme()
  var isDarkTheme by rememberSaveable { mutableStateOf(systemDark) }
  var currentScreen by rememberSaveable(stateSaver = Screen.Saver) {
    mutableStateOf<Screen>(Screen.Home)
  }

  val drawerState = rememberDrawerState(initialValue = DrawerValue.Closed)
  val scope = rememberCoroutineScope()
  val scrollState = rememberScrollState()

  // Handle system back button: return to Home screen if on subpage, or close drawer
  BackHandler(enabled = drawerState.isOpen || currentScreen != Screen.Home) {
    if (drawerState.isOpen) {
      scope.launch { drawerState.close() }
    } else {
      currentScreen = Screen.Home
      scope.launch { scrollState.scrollTo(0) }
    }
  }

  MyApplicationTheme(darkTheme = isDarkTheme) {
    ModalNavigationDrawer(
      drawerState = drawerState,
      drawerContent = {
        ModalDrawerSheet(
          modifier = Modifier.widthIn(max = 320.dp)
        ) {
          Column(
            modifier = Modifier
              .fillMaxWidth()
              .verticalScroll(rememberScrollState())
              .padding(16.dp)
          ) {
            // Drawer Header
            Column(modifier = Modifier.padding(vertical = 8.dp)) {
              Text(
                text = "MY USEFUL TOOLS",
                style = MaterialTheme.typography.titleLarge,
                fontWeight = FontWeight.Black,
                color = MaterialTheme.colorScheme.primary
              )
              Text(
                text = "Free Online Utility Portal",
                style = MaterialTheme.typography.bodySmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant
              )
            }

            HorizontalDivider(modifier = Modifier.padding(vertical = 8.dp))

            // Home Item
            NavigationDrawerItem(
              icon = { Icon(Screen.Home.icon, contentDescription = null) },
              label = { Text("Home") },
              selected = currentScreen == Screen.Home,
              onClick = {
                currentScreen = Screen.Home
                scope.launch {
                  drawerState.close()
                  scrollState.scrollTo(0)
                }
              },
              modifier = Modifier.padding(NavigationDrawerItemDefaults.ItemPadding)
            )

            Spacer(modifier = Modifier.height(12.dp))

            // Tools Section Header
            Text(
              text = "CALCULATORS",
              style = MaterialTheme.typography.labelSmall,
              fontWeight = FontWeight.Bold,
              color = MaterialTheme.colorScheme.onSurfaceVariant,
              letterSpacing = 1.sp,
              modifier = Modifier.padding(start = 12.dp, bottom = 4.dp)
            )

            Screen.allTools.forEach { tool ->
              NavigationDrawerItem(
                icon = { Icon(tool.icon, contentDescription = null) },
                label = { Text(tool.title) },
                selected = currentScreen == tool,
                onClick = {
                  currentScreen = tool
                  scope.launch {
                    drawerState.close()
                    scrollState.scrollTo(0)
                  }
                },
                modifier = Modifier.padding(NavigationDrawerItemDefaults.ItemPadding)
              )
            }

            Spacer(modifier = Modifier.height(12.dp))

            // Legal & Info Section Header
            Text(
              text = "INFORMATION & POLICIES",
              style = MaterialTheme.typography.labelSmall,
              fontWeight = FontWeight.Bold,
              color = MaterialTheme.colorScheme.onSurfaceVariant,
              letterSpacing = 1.sp,
              modifier = Modifier.padding(start = 12.dp, bottom = 4.dp)
            )

            Screen.legalPages.forEach { page ->
              NavigationDrawerItem(
                icon = { Icon(page.icon, contentDescription = null) },
                label = { Text(page.title) },
                selected = currentScreen == page,
                onClick = {
                  currentScreen = page
                  scope.launch {
                    drawerState.close()
                    scrollState.scrollTo(0)
                  }
                },
                modifier = Modifier.padding(NavigationDrawerItemDefaults.ItemPadding)
              )
            }
          }
        }
      }
    ) {
      Scaffold(
        modifier = Modifier.fillMaxSize(),
        topBar = {
          WebAddressBar(
            currentScreen = currentScreen,
            isDarkTheme = isDarkTheme,
            onToggleTheme = { isDarkTheme = !isDarkTheme },
            onNavigateHome = {
              currentScreen = Screen.Home
              scope.launch { scrollState.scrollTo(0) }
            },
            onNavigateBack = {
              currentScreen = Screen.Home
              scope.launch { scrollState.scrollTo(0) }
            },
            onOpenMenu = {
              scope.launch { drawerState.open() }
            },
            canNavigateBack = currentScreen != Screen.Home
          )
        }
      ) { innerPadding ->
        Box(
          modifier = Modifier
            .fillMaxSize()
            .padding(innerPadding),
          contentAlignment = Alignment.TopCenter
        ) {
          // Centered constraint for desktop and tablet responsiveness
          Column(
            modifier = Modifier
              .fillMaxWidth()
              .widthIn(max = 768.dp)
              .verticalScroll(scrollState)
          ) {
            when (currentScreen) {
              Screen.Home -> {
                HomeScreen(
                  onNavigateToTool = { tool ->
                    currentScreen = tool
                    scope.launch { scrollState.scrollTo(0) }
                  }
                )
              }

              Screen.AgeCalculator -> AgeCalculatorScreen()
              Screen.EmiCalculator -> EmiCalculatorScreen()
              Screen.PercentageCalculator -> PercentageCalculatorScreen()
              Screen.DiscountCalculator -> DiscountCalculatorScreen()
              Screen.BmiCalculator -> BmiCalculatorScreen()

              Screen.AboutUs,
              Screen.ContactUs,
              Screen.PrivacyPolicy,
              Screen.TermsConditions,
              Screen.Disclaimer -> LegalPageScreen(screen = currentScreen)
            }

            // Universal Footer on all pages
            AppFooter(
              onNavigate = { page ->
                currentScreen = page
                scope.launch { scrollState.scrollTo(0) }
              },
              onScrollToTop = {
                scope.launch { scrollState.animateScrollTo(0) }
              }
            )
          }
        }
      }
    }
  }
}
